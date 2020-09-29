const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
window.$.getJSON(url, {
  tags: 'name'
}, function (json) {
  window.$('DIV#character').text(json.name);
});
