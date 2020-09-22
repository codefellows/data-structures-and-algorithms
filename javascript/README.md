# Data Structures and Algorithms

## Language: `JavaScript`

### Folder and Challenge Setup

### Data Structures

For each data structure implementation

- Create a new folder under the `javascript` level, with the name of the data structure and complete your implementation there
  - i.e. `linked-list`
- Implementation (the data structure "class")
  - The implementation of the data structure must be named `index.js`
- Tests
  - Create folder named `__tests__` and within it, a test file called `[data-structure].test.js`
    - i.e. `__tests__/linked-list.test.js`
    - Your tests will then need to require the data structure you're testing
      - i.e. `const LinkedList = require('../index');

### Daily Code Challenges

Code challenges should be completed within a folder named `code-challenges` under the `javascript` level

- Daily Setup:
  - Create a new folder under the `javascript` level, with the name of the code challenge, as dictated by the challenge instructions
    - i.e. `code-challenges/reverse-ll`
  - Code Challenge Implementation
    - Name the actual challenge file with the name of the challenge, unless otherwise noted in the assignment
      - i.e. `reverse-ll.js`
      - Your challenge file will then need to require the data structure you're using to implement
      - i.e. `const LinkedList = require('../linked-list');
  - Tests
    - Create folder named `__tests__` and within it, a test file called `[challenge].test.js`
      - i.e. `__tests__/reverse-ll.test.js`
      - Your test file would require the challenge file found in the directory above.
        - i.e. `const reverse = require('../reverse-ll.js');

### Running Tests

If you setup your folders according to the above guidelines, running tests becomes a matter of deciding which tests you want to execute.  Jest does a good job at finding the test files that match what you specify in the test command

From the root of the `data-structures-and-algorithms` folder, execute the following commands:

- **Run every possible test** - `npm test`
- **Run a test for a data structure - `npm test linked-list`
- **Run a test for a specific challenge - `npm test reverse-ll`

#### Live Tests

Note that when you check your code into GitHub, all of your tests will automatically execute. These results should match your own, and will be found on the  **Actions** tab
