class HashTable:
    def __init__(self):
        self.MAX=10
        self.arr = [[] for i in range(self.MAX)]
    def get_hash(self,str):
        h = 0
        for char in str:
            h+=ord(char)
        return h % self.MAX
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h]=val
    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.arr[h]
    def __delitem__(self,key):
        h = self.get_hash(key)
        self.arr[h] = None
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0]==key:
                self.arr[h][idx] = (key,val)
                found = True
                break
        if not found:
            self.arr[h].append( (key,val))
    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0]==key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]
ht = HashTable()
ht["march 6"] = 1
ht["march 9"] = 2
ht["march 10"] = 3
ht['march 17'] = 4
print(ht["march 6"])
print(ht["march 9"])
print(ht["march 10"])
del ht["march 6"]
print(ht["march 6"])
print(ht["march 17"])


