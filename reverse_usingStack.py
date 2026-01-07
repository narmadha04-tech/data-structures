#reverse using stack
class Stack:
    def __init__(self):
        self.items=[]
    
    def push(self,val):
        if len(self.items)>=5:
            return "Stack Overflow"
        self.items.append(val)
    
    def rev(self):
        if not self.items:
            print("Stack is empty")
        else:
            rev_list = []
            while self.items: # while original stack is not empty
                rev_list.append(self.items.pop()) #popping from original stack and appending to rev_list
            return rev_list

stackObj = Stack()
stackObj.push(10)
stackObj.push(20)
stackObj.push(30)
stackObj.push(40)
print("Initial List:", stackObj.items) 
print("Reversed List:", stackObj.rev())

        