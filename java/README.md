# Data Structures and Algorithms

## Language: `Java`

### Folder/Project Setup

Each type of code challenge has slightly different instructions. Please refer to the notes and examples below for instructions for each DS&A assignment type.

### Data Structure: New Implementation

These code challenges are typically done as the first challenge following the introduction of a new data structure. You will want to create a new class for the data structure itself as well as a test class to assert its operation.

#### Implementation

- Create a new folder and class in the `datastructures` subfolder of the `main` branch of Gradle library source, with the name of the new data structure in the folder and class names, and complete your implementation there.
  - Ex. Linked Lists:
    - `lib\src\main\java\datastructures\linkedlist\LinkedList.java`

#### Tests

- Create a new folder and class in the `datastructures` subfolder of the `test` branch of Gradle library source, with the name of the new data structure in the folder and class names, and complete your test implementation there.
  - Ex. Linked Lists:
    - `lib\src\test\java\datastructures\linkedlist\LinkedListTest.java`

#### Whiteboard Diagram & README

- Include a README that describes the data structure operation.
- Include sections for each method describing inputs and outputs.
  - Include images where appropriate.

### Data Structure: Extending an implementation

Some code challenges are not so much "interview style" algorithms, but rather tasks to "extend" your base class. In these cases, you should simply be adding methods to your class along with the appropriate tests.

#### Implement a New Method

- Work within the class you created for the data structure in the `datastructures` folder.
  - Ex. Linked Lists:
    - `lib\src\main\java\datastructures\linkedlist\LinkedList.java`
- Create a new method within the class that solves the code challenge.

#### Testing Implementations

- Add to the tests written for this data structure in the `datastructures` folder.
  - Ex. Linked Lists:
    - `lib\src\test\java\datastructures\linkedlist\LinkedListTest.java`

### Code Challenge / Algorithms

Some of your daily code challenges will be of the algorithmic type, mirroring a whiteboard exam or interview.

You will be working in the `codechallenges` subfolder for all of your algorithm questions.

#### Code Challenges

- For each data structure, create a new folder and class in the `codechallenges` subfolder of the `main` branch of Gradle library source, with the name of the new data structure in the folder and class names. This is where your code challenge methods will eventually be written.
  - Ex. Linked Lists: `lib\src\main\java\codechallenges\linkedlist\LinkedListChallenges.java`
- Import the subfolder of the appropriate data structure source folder.
  - Ex. Linked Lists: (`import datastructures.linkedlist.LinkedList;`)
- For each code challenge, create a new method within that class, using the challenge name.
  - Ex. `findMiddleNode()`

#### Code Challenge Tests

- Work in the `codechallenges` subfolder of the `test` branch of Gradle library source, with the name of the new data structure in the folder and class names.
  - Ex. Linked Lists: `lib\src\test\java\codechallenges\linkedlist\LinkedListChallengesTest.java`
- Within this class, you'll add the tests appropriate for your new code challenge.

#### Whiteboards and READMEs

- Create a master "README" at the top level of your `codechallenges` folder.
  - Within, create links to a separate README for each daily challenge.
- For each challenge, create a new README.md along with your whiteboard photo/image.
  - This should describe your approach, methodologies, etc.

#### Live Tests

Create a github action to automatically run all of your tests as you check in your code. These results should match your own, and will be readily found on the  **Actions** tab.