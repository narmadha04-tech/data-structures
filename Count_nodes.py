#length of linked list

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

def length_of_linkedlist(newNode):
    count = 0
    temp = newNode
    while temp is not None:
        count += 1
        temp = temp.next
    return count
print("Length of linked list:", length_of_linkedlist(nextNode))