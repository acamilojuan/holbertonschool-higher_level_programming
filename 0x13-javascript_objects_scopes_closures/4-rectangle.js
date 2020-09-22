#!/usr/bin/node
/* Script that creates a class Rectangle that defines a rectangle
and other instance methods */

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

  rotate () {
    const aux = this.width;
    this.width = this.height;
    this.height = aux;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
