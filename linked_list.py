class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next
class linkedlist:
    def __init__(self):
        self.head = None
    def insert_at_end(self,data):
       if self.head is None:
            self.head = Node(data,None)
            return 
       itr = self.head
       while itr.next:
           itr=itr.next
       itr.next = Node(data, None) 
       node = Node(data,None)
    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node
    def Print(self):
       if self.head is None:
           print("Linked list is empty")
           return 
       itr = self.head
       llstr = ''
       while itr:
           llstr +=str(itr.data)+'-->'
           itr = itr.next
       print(llstr)
    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count
    def remove_at(self,index):
        if(index < 0 or index>=self.get_length()):
            raise Exception['indexError']
        
ll = linkedlist()
ll.insert_values(['sai','teja','varma'])
ll.Print()
print(ll.get_length())
