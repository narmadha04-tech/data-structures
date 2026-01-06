#Add new nodes to linked list
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

#adding new node at the end
def add_node(head, new_data): 
    new_node = Node(new_data)
    if head is None:
        head = new_node
        return head
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = new_node
    return head

# call add_node
head = add_node(head, 50)

# traversal to check output
temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")

#adding element using position
def add_node(head, new_data, position):
    new_node = Node(new_data)
    if position == 0:
        new_node.next = head
        head = new_node
        return head
    temp = head
    for _ in range(position - 1):
        if temp is None:
            return head
        temp = temp.next
    new_node.next = temp.next
    temp.next = new_node
    return head

# call add_node
head = add_node(head, 25, 2)

# traversal to check output
temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")