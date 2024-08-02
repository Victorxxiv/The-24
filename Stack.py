class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0


# Examples
s = Stack()
s.push(10)
s.push(20)
print(s.peek())  # 20
print(s.pop())  # 20
print(s.is_empty())  # False
