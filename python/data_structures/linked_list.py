class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
        self.head = None

    def __str__(self):

        current = self.head
        values = []

        while current:
            values.append("{ " + current.value + " }")
            current = current.next

        values.append("NULL")

        return " -> ".join(values)

    def insert(self, value):
        self.head = Node(value, self.head)

    def includes(self, value):
        current = self.head

        while current:
            if current.value == value:
                return True
            current = current.next

        return False

    def append(self, value):
        current = self.head
        node = Node(value)

        if not current:
            self.head = node
            return

        while current.next:
            current = current.next

        current.next = node

    def insert_before(self, before_value, value):
        current = self.head
        if not current:
            raise TargetError

        if current.value == before_value:
            self.head = Node(value, self.head)
            return

        while current.next:
            if current.next.value == before_value:
                current.next = Node(value, current.next)
                return
            current = current.next

        raise TargetError

    def insert_after(self, after_value, value):
        current = self.head
        while current:
            if current.value == after_value:
                current.next = Node(value, current.next)
                return
            current = current.next

        raise TargetError

    def kth_from_end(self, k):
        if k < 0:
            raise TargetError

        current = self.head
        length = 0
        while current:
            current = current.next
            length += 1
        steps_remaining = length - k - 1
        if steps_remaining < 0:
            raise TargetError

        current = self.head
        while steps_remaining:
            current = current.next
            steps_remaining -= 1

        return current.value


class TargetError(Exception):
    pass


class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_
