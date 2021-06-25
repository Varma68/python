from collections import deque
class queue:
    def __init__(self):
        self.container = deque()
    def enqueue(self,data):
        self.container.appendleft(data)
    def dequeue(self):
        return self.container.pop()
    def size(self):
        return len(self.container)
    def is_empty(self):
        return self.size()==0
    def Print(self):
        for i in range(self.size()):
            print(self.container[i], end=" ")

que = queue()
que.enqueue(1)
que.enqueue(2)
que.enqueue(3)
que.enqueue(4)
print(que.dequeue())
print(que.dequeue())
print(que.dequeue())
print(que.dequeue())


