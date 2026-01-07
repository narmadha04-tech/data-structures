#postfix calculation using stack
class Stack:
    def __init__(self):
        self.items = []
    
    def postfix_cal(self, exp):
        for ch in exp:
            # If operand
            if ch.isdigit():
                self.items.append(int(ch))
            
            # If operator
            else:
                val2 = self.items.pop()
                val1 = self.items.pop()

                if ch == '+':
                    self.items.append(val1 + val2)
                elif ch == '-':
                    self.items.append(val1 - val2)
                elif ch == '*':
                    self.items.append(val1 * val2)
                elif ch == '/':
                    self.items.append(val1 / val2)
                elif ch == '%':
                    self.items.append(val1 % val2)

        return self.items.pop()

exp = input("Enter postfix expression: ")
stackObj = Stack()
print("Postfix Evaluation:", stackObj.postfix_cal(exp))
