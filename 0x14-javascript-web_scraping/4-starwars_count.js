#!/usr/bin/node
/* Script that prints the number of movies
where the character “Wedge Antilles” is present */

const request = require('request');
const url = process.argv[2];
const id = '18';
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let count = 0;
    for (const movies of JSON.parse(body).results) {
      for (const character of movies.characters) {
        if (character.includes(id)) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
