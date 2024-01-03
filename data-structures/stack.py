class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    
    def print(self):
        for i in range(len(self.items)):
            print(self.items[i])
    
    def push(self, data):
        self.items.append(data)
    
    def pop(self):
        if self.isEmpty():
            return "Stack Is Empty"
        self.items.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return "Stack Is Empty"
        print(self.items[0])

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

print("Stack:")
stack.print()

print("\nPop:", stack.pop())

print("Peek:", stack.peek())

print("\nStack after pop:")
stack.print()