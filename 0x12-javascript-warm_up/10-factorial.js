#!/usr/bin/node
/* Script that computes and prints a factorial */

function factorial (num) {
  if (!num || num === 0) {
    return 1;
  } else {
    return (num * factorial(num - 1));
  }
}
console.log(factorial(parseInt(process.argv[2])));
