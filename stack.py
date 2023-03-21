
class Stack:
    """
    An abstract data type that is a list of elements
    organized according to the LIFO principle
    """

    def __init__(self):
        self.head = None

    def is_empty(self) -> bool:
        return self.head is None

    def push(self, data):
        new_stack = StackNode(data)
        new_stack.next = self.head
        self.head = new_stack

    def pop(self):
        if self.is_empty():
            raise IndexError('pop from empty stack')
        else:
            data = self.head.data
            self.head = self.head.next
            return data

    def size(self) -> int:
        count = 0
        if not self.is_empty():
            count += 1
            node = self.head
            while node.next:
                count += 1
                node = node.next

        return count

    def peek(self):
        if self.is_empty():
            raise IndexError('peek from empty stack')
        else:
            return self.head.data


class StackNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None
