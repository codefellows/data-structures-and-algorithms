class Node: 
  def __init__(self, value: any, next= None):
    """Creates a Node Instance with properties of value and next.
       
       input <-- value [,next]
       output --> Node instance
    """
    self.value = value
    self.next = next

class Stack:

  def __init__(self, top = None):
    """Creates a Stack Instance with a property of Top defaulting to none. 
       Value passed as an argument will create a node and assign it to the 
       self.top property
       
       input <-- value
       output --> Stack Instance

    """ 
    if top:
      self.top = Node(top)
    else:
      self.top = top


  def __str__(self) -> str:
    """ Returns a string Literal containing the value and Next of the Top Node.

    input <-- none
    output --> str
    """
    pass
  
  def __repr__(self) -> str:
    """Returns a String Description of the Instance. 
       input<-- none
       output --> str
    """
    pass

  def push(self, value: any):
    """Adds a Node to the top of the stack, assigning its next as the existing top 
       and assigning itself to the new top

       input <-- value
       output --> non-fruitful
    """ 
    pass
  
  def pop(self) -> any:
    """Removes the top Node and returns it's value, assigning the next to the top

       input <-- none
       output --> value

    """
    pass

  def peek(self) -> any:
    """Looks at the value of the top Node and returns it, DOES NOT MUTATE THE STACK
       input <-- None
       output --> value

    """
    pass

  def is_empty(self) -> bool:
    """checks for an empty stack
       input <-- None
       Output --> bool
    """
    pass