class Node:
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next
class double_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert_at_beginning(self, data):
        if self.head is None and self.tail is None:
            self.head = Node(data, None, None)
            self.tail = self.head
            return
        node = Node(data,None,self.head)
        self.head.prev = node
        self.head = node
    def insert_at_end(self,data):
        if self.head is None and self.tail is None:
            self.head = Node(data, None, None)
            self.tail = self.head
            return
        node = Node(data, self.tail, None)
        self.tail.next = node
        self.tail = node
    def get_length(self):
        count=0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count
    def remove_at(self,index):
        if index<0 or index >= self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return
        if index == self.get_length()-1:
            self.tail = self.tail.prev
            self.tail.next = None
            return

        count=0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                itr.next.prev = itr
            count+=1
            itr = itr.next
    def insert_at(self, data, index):
        if index < 0 or index >=self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_beginning(data)
            return
        if index == self.get_length()-1:
            self.insert_at_end(data)
            return
        itr = self.head
        count = 0
        while itr:
            if count == index-1:
                node = Node(data, itr, itr.next)
                itr.next = node
                node.next.prev = node
            count+=1
            itr = itr.next
    def insert_values(self, data_list):
        self.head = None
        self.tail = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        while itr:
            if(itr.data == data_after):
                node = Node(data_to_insert, itr, itr.next)
                itr.next = node
                node.next.prev = node
            itr = itr.next

    def remove_by_value(self, data):
        if self.head is None and self.tail is None:
            print("List is empty")
            return

        itr = self.head
        while itr:
            if itr.data == data:
                itr.next.prev = itr.prev
                itr.prev.next = itr.next
            itr = itr.next

    def Print_forward(self):
        if self.head is None and self.tail is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr+=str(itr.data)+"-->"
            itr = itr.next
        print(llstr)
    def Print_backward(self):
        if self.head is None and self.tail is None:
            print("List is Empty")
            return
        itr = self.tail
        llstr = ''
        while itr:
            llstr += '<--'+str(itr.data)
            itr = itr.prev
        print(llstr)
dll = double_linked_list()
dll.insert_values(["brahma",'routhu',"sai","teja","Varma"])
dll.Print_forward()
dll.insert_after_value("routhu","srinu")
dll.remove_by_value('routhu')
dll.Print_forward()
dll.get_length()
