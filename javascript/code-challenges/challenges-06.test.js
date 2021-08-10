'use strict';

/* ------------------------------------------------------------------------------------------------
CHALLENGE 1 - Review

Write a function named getNames that, given an array of people objects, uses map to return an array of names reversed.

For example:
[
{
  name: 'lloyd',
  age: 32,
  shoeSize: 12
},
{
  name: 'jamie',
  age: 21,
  shoeSize: 8
}
]

Returns: ['dyoll', 'eimaj'];
------------------------------------------------------------------------------------------------ */

const getNames = (arr) => {
  // Solution code here...
  let myArray=arr.map((element)=>{

return element.name.split("").reverse().join("");
  });
  return myArray;
};

/* ------------------------------------------------------------------------------------------------
CHALLENGE 2

Write a function that appends ' The end.' to a string, and returns the modified string. The original source string should not be modified.

------------------------------------------------------------------------------------------------ */

const appendTheEnd = (str) => {
  // Solution code here...
  let str1 = `${str} The end.`;
  return str1;
};

/* ------------------------------------------------------------------------------------------------
CHALLENGE 3

Write a function that accepts an array and copies the first element to the end of the array. The change should be reflected in the source array that was passed in to the function. That is, the function should modify the array 'in place'.

Do not use a return statement.

For example:
const a = [1, 2, 3];
appendFirstToLast(a);
console.log(a) prints [1, 2, 3, 1]
------------------------------------------------------------------------------------------------ */

const appendFirstToLast = (arr) => {
  // Solution code here...
  arr.push(arr[0]);
};

/* ------------------------------------------------------------------------------------------------
CHALLENGE 4

Write a function that accepts an object and an integer as arguments and adds a new property to the object called yearBorn. The value of the yearBorn property should be the integer that was passed in.

The change should be reflected in the source object that was passed in to the function. That is, the function should modify the object 'in place'.

Do not use a return statement.

For example:
const octavia = { fullName: 'Octavia Estelle Butler' };
addBirthYearProperty(octavia, 1947);
console.log(a) prints { fullName: 'Octavia Estelle Butler', yearBorn: 1947 }
------------------------------------------------------------------------------------------------ */

const addBirthYearProperty = (obj, year) => {
  // Solution code here...

  obj.yearBorn=year;
};

/* ------------------------------------------------------------------------------------------------
CHALLENGE 5 - Stretch Goal

Write a function that accepts an array of people objects and adds a new property called isAuthor to each object in the list. Set the value of the new property to true.

The function should modify the object in place. Do not use a return statement.

For example:
const people = [{ fullName: 'Octavia Butler' }, { fullName: 'Ray Bradbury' }];
setStatusAsAuthor(people);
console.log(people[1].isAuthor) prints true
------------------------------------------------------------------------------------------------ */

const setStatusAsAuthor = (people) => {
  // Solution code here...
};

/* ------------------------------------------------------------------------------------------------
CHALLENGE 6 - Stretch Goal

Write a function that accepts two arrays. Append the values from the second array into the first,
maintaining the ordering.

The function should modify the first array in place. Do not use a return statement.

For example:
const a = [1, 2]; NOTE: If you assign an array to a `const`, you can't re-assign it later, but you can change the values in the array.
const b = [3, 4];
append(a, b);
console.log(a) prints [1, 2, 3, 4]
------------------------------------------------------------------------------------------------ */

const append = (arr1, arr2) => {
  // Solution code here...

};

/* ------------------------------------------------------------------------------------------------
TESTS

All the code below will verify that your functions are working to solve the challenges.

DO NOT CHANGE any of the below code.

Run your tests from the console: jest challenges-02.test.js

------------------------------------------------------------------------------------------------ */

describe('Testing challenge 1', () => {
  test('It returns an array of names reversed', () => {
    expect(getNames([{name:'lloyd', age: 32, shoeSize: 12}, {name:'jamie', age:21, shoeSize: 8}])).toStrictEqual(['dyoll', 'eimaj']);
    expect(getNames([])).toStrictEqual([]);
  });
});

describe('Testing challenge 2', () => {
  test('It should append without modifying the oiginal', () => {
    const a = 'This is my story.';
    const b = appendTheEnd(a);

    expect(a).toStrictEqual('This is my story.');
    expect(b).toStrictEqual('This is my story. The end.');
  });
});

describe('Testing challenge 3', () => {
  test('It should append by modifying the oiginal', () => {
    const a = ['Yes', 'it', 'is'];
    appendFirstToLast(a);

    expect(a).toStrictEqual(['Yes', 'it', 'is', 'Yes']);
  });
});

describe('Testing challenge 4', () => {
  test('It should add a property to an object', () => {
    const a = { fullName: 'Octavia Butler' };
    addBirthYearProperty(a, 1947);

    expect(a.yearBorn).toStrictEqual(1947);
  });
});

xdescribe('Testing challenge 5', () => {
  test('It should add a property to every object in an array', () => {
    const a = [{ fullName: 'Octavia Butler' }, { fullName: 'Ray Bradbury' }, { fullName: 'Kurt Vonnegut' }];
    setStatusAsAuthor(a);

    expect(a[0].isAuthor).toStrictEqual(true);
    expect(a[1].isAuthor).toStrictEqual(true);
    expect(a[2].isAuthor).toStrictEqual(true);
  });
});

xdescribe('Testing challenge 6', () => {
  test('It should append the second array to the first', () => {
    const a = [1, 2, 3, 4];
    const b = [5, 6, 7, 8];
    append(a, b);

    expect(a).toStrictEqual([1, 2, 3, 4, 5, 6, 7, 8]);
  });
});
