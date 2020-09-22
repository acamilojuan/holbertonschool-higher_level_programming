#!/usr/bin/node
/* Script that Write a class Square that defines
a square and inherits from Square of 5-square.js */

const square = require('./5-square');

class Square extends square {
  charPrint (c) {
    if (!c) {
      this.print();
    } else {
      for (let index1 = 0; index1 < this.height; index1++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
