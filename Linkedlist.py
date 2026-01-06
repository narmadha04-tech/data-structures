#Creating Linked List and accessing its elements

class Node:
    def __init__(self, data): # Initialize a node with data and next pointer
        self.data = data # Data of the node
        self.next = None # Pointer to the next node

# Creating nodes
nextNode = Node(10)
nextNode_1 = Node(20)
nextNode_2 = Node(30)

# Order of nodes: 10 -> 20 -> 30
# Adding address of next node to current node
nextNode.next = nextNode_1
nextNode_1.next = nextNode_2 

print( nextNode.data, end = "->") # Output: 10
print( nextNode.next.data, end = "->") # Output: 20
print( nextNode.next.next.data) # Output: 30
print("None") # Indicating the end of the linked list

'''
# Order of nodes: 10 -> 30 -> 20
nextNode.next = nextNode_2
nextNode_2.next = nextNode_1

print( nextNode.data, end = "->") # Output: 10
print( nextNode.next.data, end = "->") # Output: 30
print( nextNode.next.next.data, end = "->") # Output: 20
print("None") # Indicating the end of the linked list
'''