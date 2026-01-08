#queue operations - dequeue, isEmpty, isFull, peek
class Queue:
    def __init__(self):
        self.items=[]

    def enqueue(self, val):
        if len(self.items) >= 5:
            return "Queue Overflow"
        else:
            self.items.append(val)
            return f"Enqueued Element: {val}"
    
    def dequeue(self):
        if not self.items:
            return "Queue Underflow"
        else:
            return self.items.pop(0) #pop(0) to remove first element because pop() removes last element by default

    def isEmpty(self):
        if not self.items:
            return "Is Empty"
        else:
            return "Not Empty"
    
    def isFull(self):
        if len(self.items)<5:
            return "Not Full"
        else:
            return "Is Full"
    
    def peek(self):
        if not self.items:
            return "Queue is empty"
        else:
            return self.items[0]

qObj = Queue()
print(qObj.enqueue(10))
print(qObj.enqueue(20))
print(qObj.enqueue(30))
print(qObj.enqueue(40))
print(qObj.enqueue(50))
print(qObj.enqueue(60))  # This will show queue overflow
print()
print("Dequeue element is:", qObj.dequeue())
print("Is the queue empty?:", qObj.isEmpty())
print("Is the queue full?:", qObj.isFull())
print("Peek element is:", qObj.peek())
print("Final Queue:", qObj.items)