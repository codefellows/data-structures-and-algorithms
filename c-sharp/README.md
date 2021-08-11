# Data Structures and Algorithms

## Language: `C#`

### Folder/Project Setup

Each type of code challenge has slightly different instructions. Please refer to the notes and examples below for instructions for each DS&A assignment type.

### Data Structure: New Implementation

These code challenges are typically done as the first challenge following the introduction of a new data structure. You will want to create a new class for the data structure itself as well as a test class to assert its operation.

#### Implementation

- Create a new class in the `DataStructures` project, with the name of the new data structure and complete your implementation there
  - i.e. Linked Lists:
    - `DataStructures\LinkedList.cs`

#### Tests

- Create a new class in the `DataStructuresTests` project, with the name of the new data structure
  - i.e. Linked Lists:
    - `LinkedListTests.cs`
    - Compose your `[Fact]` and `[Theory]` assertions for the data structure methods in here.

#### Whiteboard Diagram & README

- Include a README that describes the data structure operation
- Include sections for each method describing inputs and outputs
  - Include images where appropriate

### Data Structure: Extending an implementation

Some code challenges are not so much "interview style" algorithms, but rather tasks to "extend" your base class. In these cases, you should simply be adding methods to your class along with the appropriate tests.

#### Implement a New Method

- Work within the Class you created for the Data Structure in the `Implementations` project
- Create a new method within the class that solves the code challenge

#### Testing Implementations

- Add to the tests written for this data structure in the `DataStructuresTests` project

### Code Challenge / Algorithms

Some of your daily code challenges will be of the algorithmic type, mirroring a Whiteboard exam or interview.

You will be working within the `CodeChallenges` project for all of your algorithm questions.

#### Code Challenges

- For each data structure, create a new class where your code challenge methods will eventually be written
  - i.e. `LinkedLists.cs`
- Import (`using DataStructures`) your data structure implementation project
- For each code challenge, create a new method within that class, using the challenge name
  - i.e. `FindMiddleNode()`

#### Code Challenge Tests

- Work in the `CodeChallengeTests` project
  - In this project, create a new Test Class for each Data Structure.
    - i.e. `LinkedListChallengeTests`
  - Within this class, you'll add the tests appropriate for your new code challenge
    - Make `[Fact]` and `[Theory]` assertions on your challenge methods

#### Whiteboards and READMEs

- Create a master "README" at the top level of your `CodeChallenges` folder
  - Within, create links to a separate README for each daily challenge
- For each challenge, create a new README.md along with your whiteboard photo/image
  - This should describe your approach, methodologies, etc

#### Live Tests

Create a github action to automatically run all of your tests as you check in your code. These results should match your own, and will be readily found on the  **Actions** tab.
