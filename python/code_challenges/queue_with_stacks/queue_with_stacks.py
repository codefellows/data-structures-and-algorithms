from code_challenges.stacks_and_queues.stacks_and_queues import Stack, Node, InvalidOperationError

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
      self.front.push(value)
      self.rear.top = self.front.top
    else:
      curr_rear = self.rear.top
      self.rear.push(value)
      curr_rear.next = self.rear.top

  def dequeue(self):
    if self.front.top.next == None:
      raise InvalidOperationError('Method not allowed on an empty collection')
    else:  
      new_front = self.front.top.next
      temp = self.front.pop()
      self.front.push(new_front.value)
      return temp
   
      


  
    

