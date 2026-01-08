#Queue
class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, val):
        if len(self.items) >= 5:
            return "Queue Overflow"
        else:
            self.items.append(val)
            return f"Enqueued Element: {val}"

qObj = Queue()
print(qObj.enqueue(10))
print(qObj.enqueue(20))
print(qObj.enqueue(30))
print(qObj.enqueue(40))
print(qObj.enqueue(50))
print(qObj.enqueue(60))  # This will show queue overflow
print("Final Queue:", qObj.items)
