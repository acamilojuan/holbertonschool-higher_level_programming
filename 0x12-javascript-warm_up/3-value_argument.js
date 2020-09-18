#!/usr/bin/node
/* Script that prints the first argument passed to it */

if (process.argv[2] == null) {
  console.log('No argument');
} else if (process.argv[2] !== null) {
  console.log(process.argv[2]);
}
