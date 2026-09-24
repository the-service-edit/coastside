(function(){
  document.documentElement.classList.remove('no-js');

  // Nav: solid after scroll
  var nav=document.getElementById('nav');
  if(nav&&!nav.classList.contains('solid')){
    var onScroll=function(){nav.classList.toggle('scrolled',window.scrollY>60)};
    window.addEventListener('scroll',onScroll,{passive:true});onScroll();
  }

  // Mobile menu
  var menu=document.getElementById('mobMenu');
  document.querySelectorAll('[data-menu-open]').forEach(function(b){b.addEventListener('click',function(){menu.classList.add('open');b.setAttribute('aria-expanded','true')})});
  document.querySelectorAll('[data-menu-close]').forEach(function(b){b.addEventListener('click',function(){menu.classList.remove('open')})});
  document.addEventListener('keydown',function(e){if(e.key==='Escape'&&menu)menu.classList.remove('open')});

  // Fade up
  if('IntersectionObserver' in window){
    var obs=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('vis');obs.unobserve(e.target)}})},{threshold:0.08,rootMargin:'0px 0px -40px 0px'});
    document.querySelectorAll('.fade-up').forEach(function(el){obs.observe(el)});
  }else{document.querySelectorAll('.fade-up').forEach(function(el){el.classList.add('vis')})}

  // Mobile quote bar: hide when a form or the footer is on screen
  var bar=document.querySelector('.mob-bar');
  if(bar){var pre=function(){bar.classList.toggle('pre',window.scrollY<window.innerHeight*0.7)};window.addEventListener('scroll',pre,{passive:true});pre()}
  if(bar&&'IntersectionObserver' in window){
    var hideFor=document.querySelectorAll('form,.footer');var vis=new Set();
    var o2=new IntersectionObserver(function(es){es.forEach(function(e){e.isIntersecting?vis.add(e.target):vis.delete(e.target)});bar.classList.toggle('hide',vis.size>0)});
    hideFor.forEach(function(el){o2.observe(el)});
  }

  // Project filters
  var filters=document.querySelectorAll('.filter');
  if(filters.length){
    var cards=document.querySelectorAll('.proj[data-sector]');
    var apply=function(key){
      filters.forEach(function(f){f.setAttribute('aria-pressed',String(f.dataset.filter===key))});
      cards.forEach(function(c){c.hidden=!(key==='all'||c.dataset.sector.split(' ').indexOf(key)>-1)});
    };
    filters.forEach(function(f){f.addEventListener('click',function(){apply(f.dataset.filter);if(history.replaceState)history.replaceState(null,'','#'+f.dataset.filter)})});
    var h=(location.hash||'').slice(1);
    if(h&&document.querySelector('.filter[data-filter="'+h+'"]'))apply(h);
  }

  // Prefill quote form from ?need=docs
  var params=new URLSearchParams(location.search);
  if(params.get('need')==='docs'){var d=document.getElementById('need-docs');if(d)d.checked=true}
  var sec=params.get('sector');if(sec){var s=document.getElementById('sector');if(s)s.value=sec}

  // Forms: submit with fetch, fall back to a normal POST without JS
  document.querySelectorAll('form[data-ajax]').forEach(function(form){
    var started=Date.now();
    form.addEventListener('submit',function(e){
      e.preventDefault();
      var status=form.querySelector('.form-status');var btn=form.querySelector('[type=submit]');
      var show=function(msg,err){status.textContent=msg;status.className='form-status show'+(err?' err':'');status.setAttribute('tabindex','-1');status.focus()};
      if(!form.checkValidity()){form.reportValidity();return}
      var hp=form.querySelector('.hp input');if((hp&&hp.checked)||Date.now()-started<3000){show('Thanks. Your enquiry has been sent.');return}
      var data=new FormData(form);
      // Join checkbox groups into one readable line
      var groups={};form.querySelectorAll('input[type=checkbox][data-group]').forEach(function(c){if(c.checked){(groups[c.dataset.group]=groups[c.dataset.group]||[]).push(c.value)}});
      Object.keys(groups).forEach(function(k){data.set(k,groups[k].join(', '))});
      var json={};data.forEach(function(v,k){json[k]=v});
      btn.disabled=true;var label=btn.textContent;btn.textContent='Sending';
      fetch(form.action,{method:'POST',headers:{'Content-Type':'application/json','Accept':'application/json'},body:JSON.stringify(json)})
        .then(function(r){return r.json()})
        .then(function(r){
          if(r.success){form.querySelectorAll('.field,.form-row,fieldset,.form-submit,.form-note').forEach(function(el){el.style.display='none'});show(form.dataset.success||'Thanks. Your enquiry has been sent.')}
          else{show('That did not send. Please try again, or email steven@coastsidesp.com.au.',true)}
        })
        .catch(function(){show('That did not send. Please try again, or email steven@coastsidesp.com.au.',true)})
        .finally(function(){btn.disabled=false;btn.textContent=label});
    });
  });
})();
