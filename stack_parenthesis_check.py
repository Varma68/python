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
dict1={')':'(','}':'{',']':'['}
flag = False
for char in str1:
    if char in dict1.values():
        s.push(char)
    elif char in dict1.keys():
        if s.is_empty():
            print("Not balanced")
            flag = True
            break
        elif s.peek() == dict1[char]:
            s.pop()
        else:
            print("Not balanced")
            flag = True
            break
if(s.is_empty() and flag == False):
    print("balanced")
if(not s.is_empty()):
    print("Not balanced")
