from collections import deque


class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop() if not self.is_empty() else None

    def peek(self):
        return self.stack[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.stack) == 0


s = Stack()
s.push = 20
s.push = 40
print(s.peek)  # 40
print(s.pop)  # 40
print(s.is_empty())  # False
