# Data Structures and Algorithms

## Language: `JavaScript`

### Repository Setup

- Each Data Structure should be implemented separately, in a properly named folder.
  - i.e. `linked-lists`
- The root file for the implementation is then to be named for the structure i.e. `linked-list.js`
- Each implementation should have a tests folder, named `__tests__`
  - Name the test file for your implementation with the name of the data structure with a `.test.js` extension
    - i.e. `linked-lists.test.js`
- For daily challenges:
  - Each implementation should have a challenges folder, named `challenges`
  - Within the challenges folder, a subfolder bearing the name of the challenge
    - i.e. `remove-duplicates`
  - Within the proper subfolder:
    - A README.md that will house your challenge summary, whiteboard photos
    - The js file that contains your challenge code
    - A `__tests__` folder for the tests for the challenge

The final structure should resemble this as you complete the course

```bash
  data-structures-and-algorithms
  |
  ├── code-challenges
  │  └── challenge-01.test.js
  │  └── challenge-02.test.js
  │  └── ...
  |
  ├── javascript
  │   └── linked-lists
  │       └── linked-list.js
  │       └── __tests__
  │           └── linked-list.test.js
  │           └── challenge-01-remove-duplicates.test.js
  │       └── challenges
  │           └── remove-duplicates
  │               └── remove-duplicates.js
  │               └── README.md
  │               └── __tests__
  │                   └── remove-duplicates.test.js
  │           └── ...
  │   └── binary-search-trees
  │       └── index.js
  │       └── __tests__
  │           └── bst.test.js
  │       └── challenges
  │           └── fizzbuzz
  │               └── fizzbuzz.js
  │               └── README.md
  │               └── __tests__
  │                   └── fizzbuzz.test.js
  │           └── ...
  │   └── ...
  |
  ├── node_modules
  |
  ├── .github
  │   └── workflows
  │       └── javascript-tests.yml
  │
  ├── .eslintrc.json
  ├── .gitignore
  ├── package-lock.json
  ├── package.json
  └── README.md
```

### Challenge Execution and Testing

- Each day, create a new challenge folder as directed for the data structure
- Your challenge implementation must include a proper README along with any images of your whiteboard
- As you implement the challenge and your tests, you should be able to use your base implementation
  - i.e.

    ```javascript
    const LinkedList = require('../linked-list.js');
    const list = new LinkedList();
    // ...
    ```

- Run your test from the root of the `data-structures-and-algorithms` repository, as follows
  - Run All Tests: `npm test`
  - Run All Tests For One Data Structure: `npm test linked-lists`
  - Run a specific test: `npm test fizzbuzz`

### Continuous Testing

The repository contains a folder named `.github` which contains a configuration file that will automatically execute all of your tests when you check in your code to GitHub.

You can see the results of your tests online in the "Actions" tab of your repository on GitHub

> NOTE: This will be the source of your grades as well.
