import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, value):
        heapq.heappush(self.heap, value)

    def pop(self):
        if self.heap:
            return heapq.heappop(self.heap)
        else:
            return None

    def peek(self):
        if self.heap:
            return self.heap[0]
        else:
            return None

    def size(self):
        return len(self.heap)

min_heap = MinHeap()

min_heap.push(4)
min_heap.push(8)
min_heap.push(2)
min_heap.push(5)

print(min_heap.heap)

print(min_heap.pop())
print(min_heap.heap)

print(min_heap.peek())
print(min_heap.size())


import heapq

class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, value):
        heapq.heappush(self.heap, -value)

    def pop(self):
        if self.heap:
            return -heapq.heappop(self.heap)
        else:
            return None

    def peek(self):
        if self.heap:
            return -self.heap[0]
        else:
            return None

    def size(self):
        return len(self.heap)

# Example usage:
max_heap = MaxHeap()
max_heap.push(4)
max_heap.push(8)
max_heap.push(2)
max_heap.push(5)

print(max_heap.heap)

print(max_heap.pop())  
print(max_heap.heap)  

print(max_heap.peek())  
print(max_heap.size())
