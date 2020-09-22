#!/usr/bin/node
/* Script that creates a function that returns the number of occurrences in a list */

exports.nbOccurences = function (list, searchElement) {
  return list.filter(element => element === searchElement).length;
};
