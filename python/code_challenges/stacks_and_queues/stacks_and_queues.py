
class InvalidOperationError(BaseException):
  """Custom Exception "Method not allowed on an empty collection
  """
  pass

class Node: 
  """Creates a Node object for use with Stack and Queue
  """
  def __init__(self, value: any, next= None):
    """Creates a Node Instance with properties of value and next.
       
       input <-- value [,next]
       output --> Node instance
    """
    self.value = value
    self.next = next

class Stack:
  """Creates an Instance of a Stack
  """

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
    return f'Instance of Stack. Top: {self.top.value} Next: {self.top.next}'
  
  # def __repr__(self) -> str:
  #   """Returns a String Description of the Instance. 
  #      input<-- none
  #      output --> str
  #   """
  #   return f'Instance of Stack. Methods: {self.push}, {self.pop}, {self.peek}, {self.is_empty}'

  def push(self, value: any):
    """Adds a Node to the top of the stack, assigning its next as the existing top 
       and assigning itself to the new top

       input <-- value
       output --> non-fruitful
    """ 
    node = Node(value, self.top)
    self.top = node

  
  def pop(self) -> any:
    """Removes the top Node and returns it's value, assigning the next to the top

       input <-- none
       output --> value

    """
    if self.is_empty() == False:
      temp = self.top
      self.top = self.top.next
      return temp.value
    else:
      raise InvalidOperationError("Method not allowed on empty collection")

  def peek(self) -> any:
    """Looks at the value of the top Node and returns it, DOES NOT MUTATE THE STACK
       input <-- None
       output --> value

    """
    if self.is_empty() == False:
      return self.top.value
    else:
      raise InvalidOperationError("Method not allowed on empty collection")

  def is_empty(self) -> bool:
    """checks for an empty stack
       input <-- None
       Output --> bool
    """
    if not self.top:
      return True
    else:
      return False


class Queue:
  """Creates an Instance of Queue
  """

  def __init__(self):
    """Creates a Queue Instance with a properties of "front" and "rear" defaulting to none. 
    Queue must be instantiated as an empty queue, accepts no arguments
       
    input <-- none
    output --> Queue Instance

    """ 
    self.front = None 
    self.rear = None

  def __str__(self):
    """Returns String Literal with "front" and "rear" values
       input <-- none
       output --> str
    """
    return f'Queue Instance, front: {self.front.value}, rear: {self.rear.value}'

  # def __repr__(self):
  #   """Returns String Literal with a Description of the Instance
  #   input <-- none
  #   output --> str
  #   """
  #   return f'Instance of Queue, Methods {self.enqueue}, {self.dequeue}, {self.peek}, {self.is_empty}'


  def enqueue(self, value):
    """Checks for empty queue, creates a node and assigns it to the rear of the queue.
    input <-- value
    output --> non-fruitful
    """
    if not self.front:
      node = Node(value)
      self.front = node 
      self.rear = node
    else: 
      node = Node(value)
      self.rear.next = node
      self.rear = node

  def dequeue(self)-> any:
    """Removes the front node of the Queue and returns its value, re-assigning it's next as the new front node
    input <-- none
    output --> value: any
    """
    if self.is_empty() == False:
      temp = self.front
      self.front = temp.next 
      return temp.value
    else:
      raise InvalidOperationError("Method not allowed on an empty collection")

  def peek(self)-> any:
    """Returns the value of the front node. DOES NOT MUTATE THE QUEUE
    input <-- none
    output -->  value: any
    """
    if self.is_empty() == False:
      return self.front.value
    else: 
      raise InvalidOperationError("Method not allowed on an empty collection")
  
  def is_empty(self)-> bool:
    """Checks if Queue is empty and returns bool
    input <-- none
    output --> boolean
    """
    if not self.front:
      return True
    else: 
      return False