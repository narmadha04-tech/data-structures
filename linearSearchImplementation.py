#linear search implementation in python
def linear_search(arr, target):
    """
    Perform a linear search on the given array to find the target value.

    Parameters:
    arr (list): The list to search through.
    target: The value to search for.

    Returns:
    int: The index of the target if found, otherwise -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example usage
arr = list(map(int, input("Enter elements: ").split()))
target = int(input("Enter target element: "))
if (linear_search(arr, target)) != -1:
    print("Element found at index:", linear_search(arr, target))
else:
    print("Element not found in the array")