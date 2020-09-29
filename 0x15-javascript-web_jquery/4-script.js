document.getElementById('red_header').onclick(function () {
  if (window.$('header').hasClass('red')) {
    window.$('header').toggleClass('green');
  } else {
    window.$('header').toggleClass('red');
  }
});
