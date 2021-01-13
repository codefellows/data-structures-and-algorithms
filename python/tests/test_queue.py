import pytest
from code_challenges.stacks_and_queues.stacks_and_queues import Queue, InvalidOperationError


def test_enqueue():
  q = Queue()
  q.enqueue("apple")
  actual = q.front.value
  expected = "apple"
  assert actual == expected

def test_dequeue():
  #TODO: write the test
  pass

def test_peek():
  q = Queue()
  q.enqueue("apple")
  q.enqueue("banana")
  q.enqueue("cucumber")
  actual = q.peek()
  expected = "apple"
  assert actual == expected

def test_peek_when_empty():
  #TODO: test that it raises an exception when queue is empty
  pass

def test_enqueue_one():
  q = Queue()
  q.enqueue("apples")
  actual = q.peek()
  expected = "apples"
  assert actual == expected

def test_enqueue_two():
  q = Queue()
  q.enqueue("apples")
  q.enqueue("bananas")
  actual = q.peek()
  expected = "apples"
  assert actual == expected

def test_dequeue_when_empty():
  #TODO: should raise exception if attempting to dequeue empty queue
  pass

def test_dequeue_when_full():
  q = Queue()
  q.enqueue("apples")
  q.enqueue("bananas")
  actual = q.dequeue()
  expected = "apples"
  assert actual == expected
  
  pass

def test_peek_post_dequeue():
  #TODO: should return new first value if peek is called after dequeue
  pass

def test_is_empty():
  #TODO: should return True if no items enqueue
  pass

def test_exhausted():
  #TODO: fn:is_empty() should return true after all items have been dequed
  pass

 