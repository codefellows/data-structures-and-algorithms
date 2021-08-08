'use strict';

/* ------------------------------------------------------------------------------------------------
CHALLENGE 1 - Review

Write a function named addAnimal that takes in array of animals (strings) and some callback function.

This function should first create a new array. Then iterate over the input array and modify each value based on the callback function provided.

Push each updated animal string into the new array. Return the new array.

HINT: Look at the tests to see how the callback functions are used.

------------------------------------------------------------------------------------------------ */

function upper(str) {
  return str.toUpperCase();
}

function lower(str) {
  return str.toLowerCase();
}

const updateAnimal = (arr, callback) => {
  // Solution code here...
  let newArray = [];
  arr.forEach(element =>{
    newArray.push(callback(element));
  });
  return newArray;
};

/* ------------------------------------------------------------------------------------------------
CHALLENGE 2

Write a function called sortNames that takes an array of names and sorts them alphabetically. Capital letters should come before lowercase letters.

For example: 'Cat' would come before 'apple'
------------------------------------------------------------------------------------------------ */

const sortNames = (arr) => {
  // Solution code here...
  let array=arr.sort();
  return array;
};

/* ------------------------------------------------------------------------------------------------
CHALLENGE 3

Write a function called sortNumbers that takes an array of numbers and sorts them from smallest to largest.

HINT: Beware... JS default is "Lexical" ordering.
------------------------------------------------------------------------------------------------ */

const sortNumbers = (arr) => {
  // Solution code here...
  let array=arr.sort((a,b)=>{

    if (a<b){
      return-1;
    }
    if(a<b){
      return 1;
    }
    return 0;
  });
  return array;
};

/* ------------------------------------------------------------------------------------------------
CHALLENGE 4

Write a function named sortBackwards that takes in an array of numbers and returns the same array, with the numbers sorted, largest to smallest.

HINT: Do it with a custom sort callback, not with using `.reverse()`. ;)
------------------------------------------------------------------------------------------------ */

const sortBackwards = (arr) => {
  // Solution code here...
  let array=arr.sort((a,b)=>{

    if (a>b){
      return-1;
    }
    if(a<b){
      return 1;
    }
    return 0;
  });
  return array;
};

/* ------------------------------------------------------------------------------------------------
CHALLENGE 5

Write a function named alphabetize that takes in an array of strings and returns the same array with the strings sorted alphabetically.

In this alphabetization, capital letters come before lower case letters.

For example, ['Alphabet', 'Zebra', 'alphabet', 'carrot'] is correctly sorted.
------------------------------------------------------------------------------------------------ */

const alphabetize = (arr) => {
  // Solution code here...
  let newArray = arr.sort();
  return newArray;
};

/* ------------------------------------------------------------------------------------------------
CHALLENGE 6

Write a function named sortByPrice that takes in an array of objects, each of which has a 'price' property, and sorts those objects by price, lowest to highest, returning the same array.

Here is an example of the input:
[
  {name: 'Sweatshirt', price: 45},
  {name: 'Bookmark', price: 2.50},
  {name: 'Tote bag', price: 15}
];
------------------------------------------------------------------------------------------------ */

const sortByPrice = (arr) => {
  // Solution code here...
  let array=arr.sort((a,b)=>{
    if(a.price<b.price){
      return -1;
    }
    else if(a.price>b.price){

      return 1;
    }
    return 0;
  }
  );

  return array;
};

/* ------------------------------------------------------------------------------------------------
CHALLENGE 7 - Stretch Goal

Write a function named alphabetizeBetter that takes in an array of strings and returns the same array, with the strings sorted alphabetically. Capitalization should not change the sort order of two strings.

For example, ['Alphabet', 'alphabet', 'carrot', 'Zebra'] is correctly sorted, and so is ['alphabet', 'Alphabet', 'carrot', 'Zebra'].
------------------------------------------------------------------------------------------------ */

const alphabetizeBetter = (arr) => {
  // Solution code here...
};

/* ------------------------------------------------------------------------------------------------
CHALLENGE 8 - Stretch Goal

Write a function named sortByLength that takes in an array of strings and returns the same array, with the strings sorted by their length, lowest to highest.
------------------------------------------------------------------------------------------------ */

const sortByLength = (arr) => {
  // Solution code here...
};

/* ------------------------------------------------------------------------------------------------
CHALLENGE 9 - Stretch Goal

Write a function named sortNumbersByLength that takes in an array of numbers and sorts those numbers by their length.

For example, [1, 14, 0.2, -281, 54782] is only correctly sorted in that order.
------------------------------------------------------------------------------------------------ */

const sortNumbersByLength = (arr) => {
  // Solution code here...
};

/*-----------------------------------------------------------------------------------------------
CHALLENGE 10 - Stretch Goal

Write a function named sortPeople that takes in an array of Person objects, each of which has firstName, lastName, and age properties, and sorts those people by their last names. Do not worry about capitalization or first names.
------------------------------------------------------------------------------------------------ */

function Person(firstName, lastName, age) {
  this.firstName = firstName;
  this.lastName = lastName;
  this.age = age;
}

const people = [
  new Person('Wes', 'Washington', 25),
  new Person('Casey', 'Codefellow', 38),
  new Person('Stan', 'Seattle', 67),
];

const sortPeople = (arr) => {
  // Solution code here...
};

/* ------------------------------------------------------------------------------------------------
CHALLENGE 11 - Stretch Goal

Write a function named sortPeopleBetter that takes in an array of Person objects, each of which has firstName, lastName, and age properties, and sorts those people by their last names.

If two people share the same last name, alphabetize on their first name.

If two people have the same full name, the younger one should come first. Do not worry about capitalization.
------------------------------------------------------------------------------------------------ */

const sortPeopleBetter = (arr) => {
  // Solution code here...
};

/* ------------------------------------------------------------------------------------------------
CHALLENGE 12 - Stretch Goal

Write a function named sortMeetingsByDay that takes in an array of objects, each of which represents a meeting happening a particular day of the week, with a particular start time and end time.

Sort the meetings by the day on which they happen, Monday-Friday. It does not matter which order meetings come in on a particular day. For example, if there are two meetings on Monday, it does not matter which comes first.
------------------------------------------------------------------------------------------------ */

function Meeting(dayOfWeek, start, end) {
  this.dayOfWeek = dayOfWeek;
  this.start = start;
  this.end = end;
}
const meetings = [
  new Meeting('Monday', '0900', '1000'),
  new Meeting('Wednesday', '1300', '1500'),
  new Meeting('Tuesday', '1145', '1315'),
  new Meeting('Wednesday', '0930', '1000'),
  new Meeting('Monday', '0900', '0945'),
  new Meeting('Friday', '1200', '1345'),
];

const sortMeetingsByDay = (arr) => {
  // Solution code here...
};

/* ------------------------------------------------------------------------------------------------
CHALLENGE 13 - Stretch Goal

This challenge should use the array of meetings from challenge 9, above.

Sort the meetings in the order that they start. If two meetings start at the same time on the same day, the shorter meeting should come first.

You DO NOT need to use your solution to Challenge 9 in completing Challenge 10.
------------------------------------------------------------------------------------------------ */

const sortSchedule = (arr) => {
  // Solution code here...
};

/* ------------------------------------------------------------------------------------------------
TESTS

All the code below will verify that your functions are working to solve the challenges.

DO NOT CHANGE any of the below code.

Run your tests from the console: jest challenges-03.test.js
------------------------------------------------------------------------------------------------ */

describe('Testing challenge 1', () => {
  test('It should return an array of uppercase animal names', () => {
    const arr = ['BeAr', 'lIon'];
    expect(updateAnimal(arr, upper)[0]).toStrictEqual('BEAR');
    expect(updateAnimal(arr, upper)[1]).toStrictEqual('LION');
  });
  test('It should return an array of lowercase animal names', () => {
    const arr = ['BeAr', 'lIon'];
    expect(updateAnimal(arr, lower)[0]).toStrictEqual('bear');
    expect(updateAnimal(arr, lower)[1]).toStrictEqual('lion');
  });
});

describe('Testing challenge 2', () => {
  test('It should return an array of names sorted alphabetically', () => {
    expect(sortNames(['able', 'Bob'])[0]).toStrictEqual('Bob');
  });
});

describe('Testing challenge 3', () => {
  test('It should sort low-to-high the numbers in an array', () => {
    expect(sortNumbers([8, 3, 2, 9, 12, 1, 115])).toStrictEqual([1, 2, 3, 8, 9, 12, 115]);
  });
});

describe('Testing challenge 4', () => {
  test('It should sort high-to-low the numbers in an array', () => {
    const nums = [3,4,5,6,7];
    expect(sortBackwards(nums)).toStrictEqual([7,6,5,4,3]);
    expect(sortBackwards([3,2,1])).toStrictEqual([3,2,1]);
    expect(sortBackwards([12,20,3])).toStrictEqual([20, 12, 3]);
    expect(sortBackwards([])).toStrictEqual([]);
    expect(sortBackwards([1])).toStrictEqual([1]);
  });
});

describe('Testing challenge 5', () => {
  test('It should sort strings alphabetically', () => {
    expect(alphabetize(['alphabet', 'Zebra', 'Alphabet', 'carrot'])).toStrictEqual([ 'Alphabet', 'Zebra', 'alphabet', 'carrot']);
    expect(alphabetize(['alphabet','Alphabet', 'carrot'])).toStrictEqual([ 'Alphabet', 'alphabet', 'carrot']);
    expect(alphabetize([])).toStrictEqual([]);
  });
});

describe('Testing challenge 6', () => {
  test('It should sort items by their price', () => {
    expect(sortByPrice([
      {name: 'Sweatshirt', price: 45},
      {name: 'Bookmark', price: 2.50},
      {name: 'Tote bag', price: 15}
    ])).toStrictEqual([
      {name: 'Bookmark', price: 2.50},
      {name: 'Tote bag', price: 15},
      {name: 'Sweatshirt', price: 45},
    ]);
    expect(sortByPrice([{price: 12}, {price: 10}])).toStrictEqual([{price: 10}, {price: 12}]);
    expect(sortByPrice([])).toStrictEqual([]);
  });
});

xdescribe('Testing challenge 7', () => {
  test('It should alphabetize without regard to capitalization', () => {
    expect(alphabetizeBetter(['Alice', 'apple', 'alert', 'Average'])).toStrictEqual([ 'alert', 'Alice', 'apple', 'Average' ]);
    const ans = alphabetizeBetter(['alphabet', 'Zebra', 'Alphabet', 'carrot']);
    expect(ans.slice(0,2)).toEqual(expect.arrayContaining([ 'Alphabet','alphabet']));
    expect(ans.slice(2)).toStrictEqual(['carrot', 'Zebra']);
  });
});

xdescribe('Testing challenge 8', () => {
  test('It should sort strings by length', () => {
    const ans = sortByLength(['alphabet', 'Zebra', 'Alphabet', 'carrot']);
    expect(ans.slice(0,2)).toStrictEqual(['Zebra', 'carrot']);
    expect(ans.slice(2,4)).toEqual(expect.arrayContaining(['Alphabet', 'alphabet']));
    expect(sortByLength(['a', 'bc', ''])).toStrictEqual(['', 'a', 'bc']);
    expect(sortByLength(['a'])).toStrictEqual(['a']);
    expect(sortByLength([])).toStrictEqual([]);
  });
});

xdescribe('Testing challenge 9', () => {
  test('It should sort numbers by their length', () => {
    expect(sortNumbersByLength([10, 2.8, 1, -47.75])).toStrictEqual([1, 10, 2.8, -47.75]);
    expect(sortNumbersByLength([100, 2.82, 1, -47.75])).toStrictEqual([1, 100, 2.82, -47.75]);
    expect(sortNumbersByLength([1,2,3])).toEqual(expect.arrayContaining([1,2,3]));
  });
});

xdescribe('Testing challenge 10', () => {
  test('It should sort people by their last names', () => {
    expect(sortPeople(people)).toStrictEqual([
      new Person('Casey', 'Codefellow', 38),
      new Person('Stan', 'Seattle', 67),
      new Person('Wes', 'Washington', 25),
    ]);
    expect(sortPeople([{lastName: 'banana'}, {lastName: 'apple'}]))
      .toStrictEqual([{lastName: 'apple'}, {lastName: 'banana'}]);
  });
});

xdescribe('Testing challenge 11', () => {
  test('It should sort people with more strict ordering', () => {
    const family = [
      new Person('Casey', 'Codefellows', 55),
      new Person('Casey', 'Codefellows', 37),
      new Person('Charlie', 'Codefellows', 21),
      new Person('Charles', 'Codefellows', 29),
      new Person('Carol', 'Codefellow', 88),
    ];
    expect(sortPeopleBetter(family)).toStrictEqual([
      new Person('Carol', 'Codefellow', 88),
      new Person('Casey', 'Codefellows', 37),
      new Person('Casey', 'Codefellows', 55),
      new Person('Charles', 'Codefellows', 29),
      new Person('Charlie', 'Codefellows', 21),
    ]);
    expect(sortPeopleBetter([{firstName: 'andrew', lastName: 'apple'}, {firstName: 'andre', lastName: 'apple'}]))
      .toStrictEqual([{firstName: 'andre', lastName: 'apple'}, {firstName: 'andrew', lastName: 'apple'}]);
  });
});

xdescribe('Testing challenge 12', () => {
  test('It should sort meetings by the day on which they happen', () => {
    const sortedMeetings = sortMeetingsByDay(meetings);
    expect(sortedMeetings.slice(0,2)).toEqual(expect.arrayContaining([new Meeting('Monday', '0900', '0945'), new Meeting('Monday', '0900', '1000')]));
    expect(sortedMeetings[2]).toStrictEqual(new Meeting('Tuesday', '1145', '1315'));
    expect(sortedMeetings.slice(3,5)).toEqual(expect.arrayContaining([new Meeting('Wednesday', '0930', '1000'), new Meeting('Wednesday', '1300', '1500')]));
    expect(sortedMeetings[5]).toStrictEqual(new Meeting('Friday', '1200', '1345'));
  });
});

xdescribe('Testing challenge 13', () => {
  test('It should sort meetings by when they happen', () => {
    expect(sortSchedule(meetings)).toStrictEqual([
      new Meeting('Monday', '0900', '0945'),
      new Meeting('Monday', '0900', '1000'),
      new Meeting('Tuesday', '1145', '1315'),
      new Meeting('Wednesday', '0930', '1000'),
      new Meeting('Wednesday', '1300', '1500'),
      new Meeting('Friday', '1200', '1345'),
    ]);
  });
});
