front = ['(','[','{']
back = [')',']','}']

def multi_bracket_validation(input):
    
    """[Takes in a string input, returns if the string has an equal amount of (), [], {} brackets]

    Args:
        input: string

    Returns:
        [Boolean]: [True if there are equal amounts of opening and closing of the same type of brackets] """

    if type(input) != str:
        return "Not a string input"
    else:
        valOne = []
        valTwo = []

        for i in input:
            if i in front:
                valOne.append(front.index(i)+1)
            elif i in back:
                valTwo.append(back.index(i)+1)

        sumOne = sum(valOne)
        sumTwo = sum(valTwo)

        if sumOne == sumTwo:
            return True
        else:
            return False
    
### Update to this implementation:

def multi_bracket_validation(text):

    pair_map = {
        "[": "]",
        "{": "}",
        "(": ")",
    }

    # no easy access to custom stack so use List in a last-in-first-out way
    stack = [] 

    for char in text:

        if char in pair_map:

            stack.append(char)

        elif char in pair_map.values():

            if not len(stack):
                return False

            opener = stack.pop()

            if char != pair_map[opener]:
                return False

    return len(stack) == 0