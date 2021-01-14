import pytest
from queue_with_stacks.queue_with_stacks import PseudoQueue, Stack, Node, InvalidOperationError

# pq = PseudoQueue()
# #[10]->[15]->[20]
# pq.stack1.push(20)
# pq.stack1.push(15)
# pq.stack1.push(10)
# pq.enqueue(5)

def test_enqueue():
    pq = PseudoQueue()
    pq.enqueue(5)
    actual = pq.stack1.top.value
    expected = 5
    assert actual == expected

def test_dequeue():
    pq = PseudoQueue()
    pq.enqueue(5)
    pq.enqueue(3)
    pq.enqueue(1)
    actual = pq.dequeue()
    expected = 5
    assert actual == expected