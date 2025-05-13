import heapq
def KthLargest(arr, k):
    min_heap = []

    for num in arr:
        heapq.heappush(min_heap, num)

        if len(min_heap) > k:
            heapq.heappop(min_heap) # This will ensure, that the size of heap is k (Which is top K largest elements)

    return min_heap[0] # The first element of final min heap will be Kth Largest because it is the smallest among top K largest number (Please make sense of it)