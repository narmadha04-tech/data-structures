#finding kth smallest and largest number in a queue
import heapq

def kth_smallest(arr, k):
    heapq.heapify(arr) #heapify is used to convert list into heap structure
 
    for i in range(k):
        ans = heapq.heappop(arr) #pop k times to get kth smallest
    return ans

def kth_largest(arr, k):
    heap = arr[:k] # k is size of heap
    heapq.heapify(heap)
    
    for num in arr[k:]: #k to end of array
        if num > heap[0]: # compare with smallest in heap
            heapq.heappop(heap) #remove smallest
            heapq.heappush(heap, num) 
    return heap[0]

arr = [7, 2, 5, 3, 9]
k_small = 3
k_large = 2

print(k_small, "smallest:", kth_smallest(arr.copy(), k_small))
print(k_large, "largest:", kth_largest(arr.copy(), k_large))
