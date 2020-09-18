#!/usr/bin/node
/* Script that prints a square */

if (parseInt(process.argv[2])) {
  for (let index = 0; index < process.argv[2]; index++) {
    console.log('X'.repeat(parseInt(process.argv[2])));
  }
} else {
  console.log('Missing size');
}
