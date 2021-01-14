import pytest
from code_challenges.queue_with_stacks.queue_with_stacks import PseudoQueue

def test_node_import():
  node = Node('value')
  assert node.value == 'value'

def test_front_stack_empty():
  q = PseudoQueue()
  assert q.front.top == None

def test_enqueue_one():
  q = PseudoQueue()
  q.enqueue('monkey')
  assert q.front.peek()  == 'monkey'
  assert q.rear.peek() == 'monkey'

def test_enqueue_two():
  q = PseudoQueue()
  q.enqueue('monkey')
  q.enqueue('business')
  assert q.front.peek() == 'monkey'
  assert q.rear.peek() == 'business'

def test_dequeue_one():
  q = PseudoQueue()
  q.enqueue('monkey')
  q.enqueue('business')
  q.dequeue()
  assert q.front.peek() == 'business'

def test_dequeue_two():
  q = PseudoQueue()
  q.enqueue('monkey')
  q.enquque('business')
  q.enqueue('time')
  q.dequeue()
  q.dequeue()
  assert q.front.peek() == 'time'

def test_dequeue_empty_on_instantiate():
  q = PseudoQueue()
  with pytest.raises(InvalidOperationError) as e:
    q.dequeue
  assert str(e.value) == 'Method not allowed on an empty collection'

def test_dequeue_empty_after_multiple_dequeue():
  q = PseudoQueue()
  q.enqueue('monkey')
  q.enqueue('business')
  q.dequeue()
  q.dequeue()
  with pytest.raises(InvalidOperationError) as e:
    q.dequeue()
  assert str(e.value) == 'Method not allowed on an empty collection'