#delete nodes in the linked list
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

# delete node by value
def delete_node(head, value):
    if head is None:
        return head
    if head.data == value:
        return head.next
    temp = head
    while temp.next and temp.next.data != value: 
        temp = temp.next
    if temp.next:
        temp.next = temp.next.next
    return head

# call delete_node
head = delete_node(head, 20)

# traversal to check output
temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")