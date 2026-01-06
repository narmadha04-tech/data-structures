# append in linked list
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

def append(head, new_data):
    temp = head
    while temp.next is not None:
        temp = temp.next
    temp.next = Node(new_data)

# call append
append(head, 50)

# traversal to check output
temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")

