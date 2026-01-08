#heap queue implementation 
import heapq

heap = []

heapq.heappush(heap, 10)
heapq.heappush(heap, 5)
heapq.heappush(heap, 20)
heapq.heappush(heap, 1)

print(heap)              # Heap structure
print(heapq.heappop(heap))  # Removes smallest element
print(heap)