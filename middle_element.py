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

def middle_element(newNode):
    #starting both pointers at head
    slow = newNode 
    fast = newNode
    while fast is not None and fast.next is not None: # fast.next to avoid NoneType error
        slow = slow.next # move slow by one
        fast = fast.next.next # move fast by two
    return slow.data

print("Middle element of linked list using two-pointer method:", middle_element(nextNode))

''' Use two pointers, slow moves 1 step and fast moves 2 steps through the linked list; 
when fast reaches the end (None), slow will be pointing at the middle node, 
because it has traveled half the distance of the list.
'''

#using counting method
def middle_element(newNode):
    count = 0
    temp = newNode
    while temp is not None:
        count += 1
        temp = temp.next

    n = count // 2
    temp = newNode
    for i in range(n):
        temp = temp.next
    return temp.data
print("Middle element of linked list using counting method:", middle_element(nextNode))