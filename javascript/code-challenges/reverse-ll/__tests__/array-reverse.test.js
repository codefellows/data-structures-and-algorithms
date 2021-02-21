'use strict';

const reverse = require('../array-reverse.js');

describe('Array Rerverse', () => {

  it('Should reverse the array.', () => {
    let myArray = [2, 4, 6, 8, 10];
    let expected = [10, 8, 6, 4, 2];
    reverse(myArray);
    expect(myArray).toEqual(expected);
  });

});