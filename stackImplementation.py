class Stack:
    def __init__(self):
        self.items = [] #items list to store stack elements

# push method with stack overflow condition
    def push(self, val):
        if len(self.items) >= 3: # setting max size to 2 for demonstration
            return "Stack Overflow"
        else:
            self.items.append(val) # Pushing the element onto the stack
            return ("Pushed Element: ", val)
    
    def pop(self):
        if not self.items: # Check if stack is empty
            return "Stack Underflow"
        else:
            return self.items.pop()
    
    def top(self):
        if not self.items:
            return "Stack is empty"
        else:     
            return self.items[-1] 
    
    def peek(self):
        if not self.items:
            return "Stack is empty"
        else:
            return self.items[-1]
    
itemObj = Stack()
print(itemObj.push(10))
print(itemObj.push(20))
print(itemObj.push(30))
print(itemObj.push(40)) # This should show stack overflow
print()
print("Top element is:", itemObj.top())
print("Peek element is:", itemObj.peek())
print("Popped element is:", itemObj.pop())
print("Final Stack:", itemObj.items)

                  




'''
stack = []
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
stack.append(50)
stack.append(60)
print("Initial stack:", stack)
print("Popped element:", stack.pop()) #popping and printing the popped element. returns 60
print(stack.pop(3)) #using index
print("Final stack:", stack) #printing stack after popping
print("Top element:", stack[-1]) #top element is last element in list
'''