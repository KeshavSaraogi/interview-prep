class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head is None
    
    def print(self):
        curr = self.head
        while (curr):
            print(curr.data)
            curr = curr.next

    def insert(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = newNode

    def delete(self, data):
        if self.head is None:
            return "Linked List Is Empty"
        
        if self.head.data == data:
            self.head = self.head.next
            
        curr = self.head
        while curr.next and curr.next.data != data:
            curr = curr.next
        
        if curr.next:
            curr.next = curr.next.next
        else:
            print(f"{data} Not Found")
    
linked_list = LinkedList()

linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)
linked_list.insert(0)

linked_list.print()

linked_list.delete(2)
linked_list.delete(4)

linked_list.print()