from .queue import Queue
from .stack import Stack

def splat(word):
    return list(word)

def multi_bracket_validation(strang):
    """This function should split the list that is given, push the bracket characters into a queue, traverse the queue to see if opening brackets are closed"""
    list_strang = splat(strang)
    brackets_q = Queue()
    square = Stack()
    curly = Stack()
    curved = Stack()
    for letter in list_strang:
        if letter is "{" or "}" or "(" or ")" or "[" or "]":
            brackets_q.enqueue(letter)
    # Enqueue all of the curly brackets

    while brackets_q.front:
        which_bracket = brackets_q.dequeue()
        if which_bracket == "(":
            curved.push("(")
        if which_bracket == "{":
            curly.push("{")
        if which_bracket == "[":
            square.push("[")
        #Cases to push in opening brackets. We are pushing each of these into their own stack.

        if which_bracket == "}":
            if curly.is_empty() is False:
                curly.pop()
            else:
                return False

        if which_bracket == ")":
            if curved.is_empty() is False:
                curved.pop()
            else:
                return False

        if which_bracket == "]":
            if square.is_empty() is False:
                square.pop()
            else:
                return False
        #Cases for dealing with closing brackets.


    return True


if __name__ == "__main__":
    print(multi_bracket_validation("[potato]"))
