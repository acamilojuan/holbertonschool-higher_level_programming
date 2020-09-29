const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
window.$.getJSON(url, function (data) {
  window.$.each(data.results, function (i, item) {
    window.$('UL#list_movies').append('<li>' + item.title + '</li>');
  });
});
