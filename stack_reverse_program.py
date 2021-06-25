from collections import deque
class Stack:
    def __init__(self):
        self.container = deque()
    def push(self, val):
        self.container.append(val)
    def pop(self):
        return self.container.pop()
    def peek(self):
        return self.container[-1]
    def is_empty(self):
        return len(self.container)==0
    def size(self):
        return len(self.container)
s = Stack()
str1 = input()
for char in str1:
    s.push(char)
while not s.is_empty():
    print(s.pop(),end="")
