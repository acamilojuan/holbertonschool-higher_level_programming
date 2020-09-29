const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
window.$.getJSON(url, function (data) {
  window.$('DIV#hello').text(data.hello);
});
