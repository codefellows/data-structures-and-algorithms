from stacks_and_queues.stacks_and_queues import Stack, Node, InvalidOperationError

class PseudoQueue:
  """Creates instance of Queue using stacks to track front and rear of queue
  """
  def __init__(self)-> object:
    """PseudoQueue instance. front and back are represented by stack objects
    """
    self.front = Stack()
    self.rear = Stack()
  
  def __str__(self)-> str:
    """String Literal showing PseudoQueue instance current front and back 
    """
    return f'A PseudoQueue instance current front value: {self.front.peek()}current rear value: {self.rear.peek()}'

  def enqueue(self, value):
    """Adds a node to the PseudoQueue instance
       input <-- any
       output --> non-fruitful (mutates instance of PseudoQueue in place)
    """ 
    if not self.front.top:
      node = Node(value)
      self.front.push(node)
      self.rear.push(node)
    else:
      node = Node(value)
      self.rear.top.next = node
      self.rear.push(node)

    

