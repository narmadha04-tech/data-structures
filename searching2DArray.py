#searching in 2D Array in python

def search_2d_array(matrix, target):
    """
    Perform a search on the given 2D array (matrix) to find the target value.

    Parameters:
    matrix (list of list): The 2D list (matrix) to search through.
    target: The value to search for.

    Returns:
    tuple: The (row, column) index of the target if found, otherwise (-1, -1).
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == target:
                return (i, j)
    return (-1, -1)

# Example usage
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix = []
print("Enter the elements row-wise:")
for i in range(rows): # 0 to rows-1
    row = list(map(int, input().split())) # 0 to cols-1
    matrix.append(row) # append the row to the matrix
target = int(input("Enter target element: "))
result = search_2d_array(matrix, target)
if result != (-1, -1):
    print("Element found at index:", result)
else:
    print("Element not found in the array")

