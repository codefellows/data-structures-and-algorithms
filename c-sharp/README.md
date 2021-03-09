# Data Structures and Algorithms

## Language: `C#`

### Folder/Project Setup

Each type of code challenge has slightly different instructions. Please refer to the notes and examples below for instructions for each DS&A assignment type.

### Data Structure: New Implementation

These code challenges are typically done as the first challenge following the introduction of a new data structure. You will want to create a new class for the data structure itself as well as a test class to assert its operation.

#### Implementation

- Create a new class in the `DataStructures\Implementations` project, with the name of the new data structure and complete your implementation there
  - i.e. Linked Lists:
    - `DataStructures\Implementations\LinkedList.cs`
#### Tests

- Create a new class in the `DataStructures\DataStructuresTests` project, with the name of the new data structure
  - i.e. Linked Lists:
    - `DataStructures\Implementations\LinkedListTests.cs`
    - Compose your `[Fact]` and `[Theory]` assertions for the data structure methods in here.

#### Whiteboard Diagram & README

- Include a README that describes the data structure operation
- Include sections for each method describing inputs and outputs
  - Include images where appropriate

### Data Structure: Extending an implementation

Some code challenges are not so much "interview style" algorithms, but rather tasks to "extend" your base class. In these cases, you should simply be adding methods to your class along with the appropriate tests.

#### Implementation

- New Method: Work within the Class you created for the Data Structure in the `Implementations` project
  - Create a new method within the class that solves the code challenge

#### Tests

  - Add to the tests written for this data structure in the `DataStructuresTests` project

#### Whiteboard Diagram & README

  - Include this as an addendum to the README for the class implementation

### Code Challenge / Algorithm

Some of your daily code challenges will be of the algorithmic type, mirroring a Whiteboard exam or interview.

### Folder/Project Setup

You will be working within the `CodeChallenges` folder for all of your algorithm questions.  Within this folder are multiple projects

#### Code Challenges

- `DataStructure`
  - Each data structure should have a challenges project created within this folder, with a program file
  - i.e. `CodeChallenges\LinkedLists\Program.cs`
  - Import (`using DataStructures`) your data structure implementation project
  - Write a method for each code challenge in the Program.cs file

#### Tests

- `CodeChallengeTests`
  - In this project, create a new Test Class for each Data Structure.
  - Within this class, you'll add a new method for each of your daily challenges
    - i.e. `CodeChallengeTests\LinkListChallengeTests.cs`
    - These classes should include (`using...`) your challenge `Program.cs` class
    - Make `[Fact]` and `[Theory]` assertions on your challenge methods

#### Whiteboards and READMEs

- Create a master "README" at the top level of your `CodeChallenges` folder
  - Within, create links to a separate README for each daily challenge
- For each challenge, create a new README.md along with your whiteboard photo/image
  - This should describe your approach, methodologies, etc


#### Live Tests

Create a github action to automatically run all of your tests as you check in your code. These results should match your own, and will be readily found on the  **Actions** tab.
