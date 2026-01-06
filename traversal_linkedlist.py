# Traversing a linked list in Python (accessing its elements)
 
class Node:
    def __init__(self, data): 
        self.data = data 
        self.next = None 

# Creating nodes
nextNode = Node(10)
nextNode_1 = Node(20)
nextNode_2 = Node(30)

# Adding address of next node to current node
nextNode.next = nextNode_1
nextNode_1.next = nextNode_2 

#traversing the linked list
temp = nextNode
while temp is not None:
    print(temp.data, end="->")
    temp = temp.next 
print("None") # Indicating the end of the linked list