import pytest
from stacks_and_queues.stacks_and_queues import Queue, InvalidOperationError


def test_enqueue():
  q = Queue()
  q.enqueue("apple")
  actual = q.front.value
  expected = "apple"
  assert actual == expected

def test_dequeue():
  #TODO: write the test
  q = Queue()
  q.enqueue("apple")
  q.enqueue("banana")
  q.dequeue()
  actual = q.peek()
  expected = "apple"
  assert actual == expected


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
  q = Queue()
  with pytest.raises(InvalidOperationError) as e:
    q.peek()
  assert str(e.value) == "Method cannot be called on an empty collection"

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
  q = Queue()
  with pytest.raises(InvalidOperationError) as e:
    q.dequeue()
  assert str(e.value) == "Method cannot be called on an empty Collection"
  

def test_dequeue_when_full():
  q = Queue()
  q.enqueue("apples")
  q.enqueue("bananas")
  actual = q.dequeue()
  expected = "apples"
  assert actual == expected
  
 

def test_peek_post_dequeue():
  #TODO: should return new first value if peek is called after dequeue
  q = Queue()
  q.enqueue("apple")
  q.enqueue("banana")
  q.enqueue("cucumber")

  q.dequeue()
  actual = q.peek()
  expected = "banana"
  assert actual == expected


def test_is_empty():
  #TODO: should return True if no items enqueue
  q = Queue()
  assert q.is_empty() == True

def test_exhausted():
  #TODO: fn:is_empty() should return true after all items have been dequed
  q = Queue()
  q.enqueue("apple")
  q.enqueue("banana")
  q.dequeue()
  q.dequeue()
  assert q.is_empty() == True

 