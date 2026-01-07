#reverse linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# create nodes
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

# traversal to check initial linked list
temp = head
while temp:
    
    print( temp.data, end=" -> ")
    temp = temp.next
print("None")

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node