#!/usr/bin/node
/* Script that creates a function that returns the number of occurrences in a list */

exports.esrever = function (list) {
  const reversed = [];
  for (let index = list.length; index >= 0; index--) {
    reversed.push(list[index]);
  }
  return reversed;
};
