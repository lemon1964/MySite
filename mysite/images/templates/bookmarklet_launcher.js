(function(){
  if(!window.bookmarklet) {
    bookmarklet_js = document.body.appendChild(document.createElement('script'));
    bookmarklet_js.src = 'https://mysite-web-vubo.onrender.com/static/js/bookmarklet.js?r=' + Math.floor(Math.random() * 9999999999999999);
  }
  else {
    bookmarkletLaunch();
  }
})();
