/* Coastside V3: one small script, no dependencies. */
(function(){
  var d=document,w=window,root=d.documentElement;
  root.classList.remove('no-js');root.classList.add('js');

  /* ---------- storage that never throws ---------- */
  function get(s,k){try{return JSON.parse(w[s].getItem(k))}catch(e){return null}}
  function set(s,k,v){try{w[s].setItem(k,JSON.stringify(v))}catch(e){}}

  /* ---------- analytics: dataLayer events (GA4 reads these via gtag/GTM at launch) ---------- */
  w.dataLayer=w.dataLayer||[];
  function track(name,params){
    var p=params||{};p.page_path=location.pathname;p.page_type=d.body.dataset.type||'';
    w.dataLayer.push(Object.assign({event:name},p));
    if(w.gtag)w.gtag('event',name,p);
    if(/localhost|127\.0\.0\.1/.test(location.hostname))console.info('[track]',name,p);
  }
  w.csTrack=track;

  /* ---------- attribution: first and last touch ---------- */
  (function(){
    var q=new URLSearchParams(location.search),keys=['utm_source','utm_medium','utm_campaign','utm_term','utm_content','gclid'];
    var touch={};keys.forEach(function(k){if(q.get(k))touch[k]=q.get(k)});
    var ref=d.referrer&&d.referrer.indexOf(location.host)<0?d.referrer:'';
    var now={landing_page:location.pathname,referrer:ref,ts:new Date().toISOString()};
    if(Object.keys(touch).length||ref){Object.assign(now,touch);if(!get('localStorage','cs_first'))set('localStorage','cs_first',now);set('sessionStorage','cs_last',now)}
    if(!get('localStorage','cs_first'))set('localStorage','cs_first',now);
    if(!get('sessionStorage','cs_last'))set('sessionStorage','cs_last',now);
    var trail=get('sessionStorage','cs_trail')||[];trail.push(location.pathname);set('sessionStorage','cs_trail',trail.slice(-12));
  })();
  function attribution(){
    var f=get('localStorage','cs_first')||{},l=get('sessionStorage','cs_last')||{},t=get('sessionStorage','cs_trail')||[];
    var prev=t.length>1?t[t.length-2]:'';
    return {first_touch:JSON.stringify(f),last_touch:JSON.stringify(l),landing_page:l.landing_page||'',referrer:l.referrer||'',
      utm_source:l.utm_source||f.utm_source||'',utm_medium:l.utm_medium||f.utm_medium||'',utm_campaign:l.utm_campaign||f.utm_campaign||'',
      utm_term:l.utm_term||'',utm_content:l.utm_content||'',gclid:l.gclid||f.gclid||'',source_page:prev,page_trail:t.join(' > ')};
  }

  /* ---------- page-level events ---------- */
  var type=d.body.dataset.type;
  if(type==='project')track('project_viewed',{project:d.body.dataset.slug});
  if(type==='builder-pack')track('builder_pack_viewed');
  d.addEventListener('click',function(e){
    var a=e.target.closest('a,button');if(!a)return;
    var h=a.getAttribute('href')||'';
    if(h.indexOf('tel:')===0)track('phone_click');
    else if(h.indexOf('mailto:')===0)track('email_click');
    else if(/capability-statement\.pdf$/.test(h))track('capability_downloaded');
    if(a.dataset.track)track(a.dataset.track,{label:a.dataset.label||''});
  });

  /* ---------- hero entrance + video respects reduced motion ---------- */
  var rises=d.querySelectorAll('.rise');
  if('IntersectionObserver' in w){var ro=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');ro.unobserve(e.target)}})},{threshold:.1});rises.forEach(function(el){ro.observe(el)})}
  else rises.forEach(function(el){el.classList.add('in')});
  var hv=d.querySelector('.vhero-video');
  if(hv&&w.matchMedia&&w.matchMedia('(prefers-reduced-motion: reduce)').matches){hv.removeAttribute('autoplay');hv.pause()}

  /* ---------- hero gallery drift: slides across and back, 30s+ each way ---------- */
  var track=d.querySelector('.shero-track');
  if(track){
    var strip=track.parentNode;
    var setDrift=function(){
      var dist=Math.max(0,track.scrollWidth-strip.clientWidth);
      track.style.setProperty('--dist',dist+'px');
      track.style.setProperty('--dur',Math.max(30,Math.round(dist/110))+'s');
      track.classList.toggle('drift',dist>0);
    };
    setDrift();w.addEventListener('load',setDrift);
    var rt;w.addEventListener('resize',function(){clearTimeout(rt);rt=setTimeout(setDrift,150)});
    if('IntersectionObserver' in w){new IntersectionObserver(function(es){track.style.animationPlayState=es[0].isIntersecting?'':'paused'}).observe(strip)}
  }

  /* ---------- nav ---------- */
  var nav=d.querySelector('.nav');
  if(nav){var onS=function(){nav.classList.toggle('compact',w.scrollY>40)};w.addEventListener('scroll',onS,{passive:true});onS()}
  var mnav=d.getElementById('mnav'),tog=d.querySelector('.nav-toggle');
  function closeNav(){mnav.classList.remove('open');tog.setAttribute('aria-expanded','false');d.body.style.overflow='';tog.focus()}
  if(tog&&mnav){
    tog.addEventListener('click',function(){mnav.classList.add('open');tog.setAttribute('aria-expanded','true');d.body.style.overflow='hidden';mnav.querySelector('a').focus()});
    mnav.querySelector('.close').addEventListener('click',closeNav);
    d.addEventListener('keydown',function(e){if(e.key==='Escape'&&mnav.classList.contains('open'))closeNav()});
  }

  /* ---------- mobile CTA bar: hide over forms and footer ---------- */
  var bar=d.querySelector('.mbar');
  if(bar&&'IntersectionObserver' in w){
    var seen=new Set();var io=new IntersectionObserver(function(es){es.forEach(function(e){e.isIntersecting?seen.add(e.target):seen.delete(e.target)});bar.classList.toggle('hide',seen.size>0)});
    d.querySelectorAll('form,.footer,.cta,.vhero,.shero').forEach(function(el){io.observe(el)});
  }

  /* ---------- project filters (URL-driven, work without JS as plain links) ---------- */
  var fb=d.querySelector('.filterbar');
  if(fb){
    var sels=fb.querySelectorAll('select'),cards=d.querySelectorAll('.proj-grid .card'),count=fb.querySelector('.filter-count'),empty=d.querySelector('.empty');
    var apply=function(push){
      var f={},n=0;sels.forEach(function(s){if(s.value)f[s.name]=s.value});
      cards.forEach(function(c){
        var ok=Object.keys(f).every(function(k){return (' '+(c.dataset[k]||'')+' ').indexOf(' '+f[k]+' ')>-1});
        c.hidden=!ok;if(ok)n++;
      });
      if(count)count.textContent=n+' of '+cards.length+' projects';
      if(empty)empty.classList.toggle('show',n===0);
      if(push){var q=new URLSearchParams(f).toString();history.replaceState(null,'',location.pathname+(q?'?'+q:''));track('filter_used',f)}
    };
    var q=new URLSearchParams(location.search);sels.forEach(function(s){if(q.get(s.name))s.value=q.get(s.name);s.addEventListener('change',function(){apply(true)})});
    var rs=fb.querySelector('.filter-reset');if(rs)rs.addEventListener('click',function(){sels.forEach(function(s){s.value=''});apply(true)});
    apply(false);
  }

  /* ---------- forms ---------- */
  function fieldOf(el){return el.closest('.field')}
  function validate(scope){
    var ok=true,first=null;
    scope.querySelectorAll('input,select,textarea').forEach(function(el){
      if(el.closest('[data-show-if]:not(.shown)')&&root.classList.contains('js'))return;
      var f=fieldOf(el);if(!f)return;
      var bad=!el.checkValidity();
      if(el.type==='radio'){var g=scope.querySelectorAll('input[name="'+el.name+'"]');bad=el.required&&![].some.call(g,function(r){return r.checked})}
      f.classList.toggle('invalid',bad);
      if(bad){ok=false;if(!first)first=el}
    });
    if(first){first.focus();}
    return ok;
  }
  function showIf(form){
    form.querySelectorAll('[data-show-if]').forEach(function(el){
      var parts=el.dataset.showIf.split('='),name=parts[0],vals=parts[1].split('|');
      var chosen=[].map.call(form.querySelectorAll('[name="'+name+'"]'),function(i){return (i.type==='radio'||i.type==='checkbox')?(i.checked?i.value:null):i.value}).filter(Boolean);
      var on=chosen.some(function(v){return vals.indexOf(v)>-1});
      el.classList.toggle('shown',on);
    });
  }
  function collect(form){
    var data={};
    new FormData(form).forEach(function(v,k){if(v instanceof File)return;if(data[k]){data[k]+=', '+v}else data[k]=v});
    form.querySelectorAll('[data-show-if]:not(.shown) [name]').forEach(function(el){delete data[el.name]});
    var files=form.querySelector('input[type=file]');
    if(files&&files.files.length)data.documents=[].map.call(files.files,function(f){return f.name+' ('+Math.round(f.size/1024)+' KB)'}).join(', ');
    Object.assign(data,attribution());
    data.submitted_from=location.pathname;
    return data;
  }
  function send(form,data){
    var st=form.querySelector('.status'),btn=form.querySelector('[type=submit]');
    btn.disabled=true;var lbl=btn.textContent;btn.textContent='Sending';
    return fetch(form.action,{method:'POST',headers:{'Content-Type':'application/json',Accept:'application/json'},body:JSON.stringify(data)})
      .then(function(r){return r.json()}).then(function(r){
        if(!r.success)throw 0;
        track(form.dataset.event||'form_submitted',{lead_type:data.lead_type||''});
        if(form.dataset.next){location.href=form.dataset.next;return}
        form.querySelectorAll('.field,.row2,.btns,fieldset,.step-nav').forEach(function(el){el.style.display='none'});
        st.textContent=form.dataset.success||'Sent. Thank you.';st.className='status show';st.setAttribute('tabindex','-1');st.focus();
      }).catch(function(){st.textContent='That did not send. Please try again, or email '+form.dataset.fallback+'.';st.className='status show err';st.focus()})
      .finally(function(){btn.disabled=false;btn.textContent=lbl});
  }

  d.querySelectorAll('form[data-ajax]').forEach(function(form){
    var started=Date.now();
    showIf(form);form.addEventListener('change',function(){showIf(form)});
    form.querySelectorAll('input,select,textarea').forEach(function(el){el.addEventListener('input',function(){var f=fieldOf(el);if(f)f.classList.remove('invalid')})});

    // Prefill from query string (?service=external-rendering&sector=multi&need=docs)
    var q=new URLSearchParams(location.search);
    q.forEach(function(v,k){form.querySelectorAll('[name="'+k+'"]').forEach(function(el){if(el.type==='checkbox'||el.type==='radio'){if(el.value===v)el.checked=true}else el.value=v})});
    showIf(form);

    // Stepper
    var steps=form.querySelectorAll('.step'),cur=0,bar=d.querySelectorAll('.stepper li');
    function go(i,focus){
      steps.forEach(function(s,j){s.classList.toggle('on',j===i)});
      bar.forEach(function(b,j){b.classList.toggle('on',j===i);b.classList.toggle('done',j<i);if(j===i)b.setAttribute('aria-current','step');else b.removeAttribute('aria-current')});
      cur=i;if(focus){var h=steps[i].querySelector('h2');if(h){h.setAttribute('tabindex','-1');h.focus({preventScroll:true})}
      var top=form.getBoundingClientRect().top+w.scrollY-100;if(w.scrollY>top)w.scrollTo(0,top);}
      set('sessionStorage','cs_quote_step',i);
    }
    if(steps.length){
      go(0);var started_t=false;
      form.addEventListener('focusin',function(){if(!started_t){started_t=true;track('quote_started')}});
      form.querySelectorAll('.next').forEach(function(b){b.addEventListener('click',function(){if(validate(steps[cur])){track('quote_step_completed',{step:cur+1});go(cur+1,true)}})});
      form.querySelectorAll('.back').forEach(function(b){b.addEventListener('click',function(){go(cur-1,true)})});
    }

    // Files: drag and drop, list
    var drop=form.querySelector('.drop'),fin=drop&&drop.querySelector('input[type=file]'),list=form.querySelector('.files');
    if(drop){
      var render=function(){list.innerHTML='';[].forEach.call(fin.files,function(f){var li=d.createElement('li');var a=d.createElement('span');a.textContent=f.name;var b=d.createElement('span');b.textContent=(f.size/1048576).toFixed(1)+' MB';li.appendChild(a);li.appendChild(b);list.appendChild(li)});if(fin.files.length)track('plans_uploaded',{count:fin.files.length})};
      drop.addEventListener('click',function(e){if(e.target!==fin)fin.click()});
      drop.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();fin.click()}});
      ['dragenter','dragover'].forEach(function(t){drop.addEventListener(t,function(e){e.preventDefault();drop.classList.add('over')})});
      ['dragleave','drop'].forEach(function(t){drop.addEventListener(t,function(e){e.preventDefault();drop.classList.remove('over')})});
      drop.addEventListener('drop',function(e){try{fin.files=e.dataTransfer.files}catch(x){}render()});
      fin.addEventListener('change',render);
    }

    form.addEventListener('submit',function(e){
      e.preventDefault();
      var scope=steps.length?steps[cur]:form;
      if(!validate(scope))return;
      var hp=form.querySelector('.hp input');
      if((hp&&hp.checked)||Date.now()-started<3000){return}
      send(form,collect(form));
    });
  });
})();
