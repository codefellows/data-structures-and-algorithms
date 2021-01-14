import pytest
from code_challenges.queue_with_stacks.queue_with_stacks import PseudoQueue
from code_challenges.stacks_and_queues.stacks_and_queues import InvalidOperationError


def test_front_stack_empty():
  q = PseudoQueue()
  assert q.front.top == None

def test_enqueue_first_node():
  q = PseudoQueue()
  q.enqueue('monkey')
  actual1 = q.front.peek()
  expected1 = 'monkey'
  assert actual1 == expected1
  actual2 = q.rear.peek()
  expected2 = 'monkey'
  assert actual2 == expected2

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
  actual1 = q.dequeue()
  expected1 = 'monkey'
  assert actual1 == expected1


def test_dequeue_two():
  q = PseudoQueue()
  q.enqueue('monkey')
  q.enqueue('business')
  q.enqueue('time')

  q.dequeue()
  
  actual1 = q.dequeue()
  expected1 = 'business'
  assert actual1 == expected1


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