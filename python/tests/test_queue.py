import pytest
from code_challenges.stacks_and_queues.stacks_and_queues import Queue, InvalidOperationError


def test_enqueue():
  q = Queue()
  q.enqueue("apple")
  actual = q.front.value
  expected = "apple"
  assert actual == expected

def test_dequeue():
  q = Queue()
  q.enqueue("apple")
  q.enqueue("banana")
  q.dequeue()
  actual = q.peek()
  expected = "banana"
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
  q = Queue()
  with pytest.raises(InvalidOperationError) as e:
    q.peek()
  assert str(e.value) == "Method not allowed on an empty collection"

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
  q = Queue()
  with pytest.raises(InvalidOperationError) as e:
    q.dequeue()
  assert str(e.value) == "Method not allowed on an empty collection"
  

def test_dequeue_when_full():
  q = Queue()
  q.enqueue("apples")
  q.enqueue("bananas")
  actual = q.dequeue()
  expected = "apples"
  assert actual == expected
  
 

def test_peek_post_dequeue():
  q = Queue()
  q.enqueue("apple")
  q.enqueue("banana")
  q.enqueue("cucumber")

  q.dequeue()
  
  actual = q.peek()
  expected = "banana"
  assert actual == expected


def test_is_empty():
  q = Queue()
  assert q.is_empty() == True

def test_exhausted():
  q = Queue()
  q.enqueue("apple")
  q.enqueue("banana")
  q.dequeue()
  q.dequeue()
  assert q.is_empty() == True

 