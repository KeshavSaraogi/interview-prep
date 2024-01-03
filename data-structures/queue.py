class Queue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

    def print(self):
        for i in range(len(self.items)):
            print(self.items[i])

    def enqueue(self, data):
        self.items.append(data)
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue Is Empty"
        return self.items.pop(0)
    
    def seek(self):
        if self.isEmpty():
            return "Queue Is Empty"
        print(self.items[0])

queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)

queue.print()

queue.dequeue()
queue.seek()

queue.print()

