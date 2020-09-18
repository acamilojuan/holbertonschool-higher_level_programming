#!/usr/bin/node
/* Script that prints x times “C is fun” */

const string = 'C is fun';
if (process.argv[2] == null) {
  console.log('Missing number of occurrences');
} else {
  for (let index = 0; index < process.argv[2]; index++) {
    console.log(string);
  }
}
