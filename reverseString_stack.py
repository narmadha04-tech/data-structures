def reverse(s):
    stack = []

    for ch in s:
        stack.append(ch)

    rev_str = ""
    while stack:
        rev_str += stack.pop()
    return rev_str

string = input("Enter the string: ")
print("Reversed string is:", reverse(string))

