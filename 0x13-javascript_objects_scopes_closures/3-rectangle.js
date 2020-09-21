#!/usr/bin/node
// Script that creates a class Rectangle that defines a rectangle //

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let index1 = 0; index1 < this.height; index1++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
