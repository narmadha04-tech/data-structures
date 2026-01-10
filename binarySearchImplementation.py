#binary search implementation in python
def binary_search(arr, target):
    """
    Perform a binary search on the given sorted array to find the target value.

    Parameters:
    arr (list): The sorted list to search through.
    target: The value to search for.

    Returns:
    int: The index of the target if found, otherwise -1.
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right)// 2 
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = list(map(int, input("Enter elements: ").split()))
target = int(input("Enter target element: "))
#sort the array to ensure it is sorted
arr.sort()
if (binary_search(arr, target)) != -1:
    print("Element found at index:", binary_search(arr, target))
else:
    print("Element not found in the array")

# Note: The input array must be sorted for binary search to work correctly.
