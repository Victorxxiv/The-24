class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def is_empty(self):
        return len(self.queue) == 0


# Example
q = Queue()
q.enqueue(20)
q.enqueue(30)
print(q.dequeue())  # 20
print(q.is_empty())  # False
