#check balanced parenthesis using stack

class Stack:
    def __init__(self):
        self.items=[]
    
    def paranthesis_check(self, exp):
        count=0
        for ch in exp:
            if ch == '(' or ch == '{' or ch == '[':
                count += 1
            elif ch == ')' or ch == '}' or ch == ']':
                count -= 1

        if count < 0:
            return False   # extra ')'
        return count == 0 # balanced if count is 0
exp = "{[(a+b)*(c-d)}"
stackObj = Stack()
if stackObj.paranthesis_check(exp): # calling paranthesis_check method
    print("Balanced Paranthesis")
else:
    print("Not Balanced Paranthesis")