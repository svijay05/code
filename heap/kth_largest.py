"""

Find K largest (or smallest) elements in array.

Solution 1: sort it using merge sort or heap sort and return array[k-1]

array.sort()
return array[k-1]

Time complexity for this solution will be o(nlogn)

Solution 2:  Construct max heap 

heap construction - O(n)

In Heap 
insert o(log n),
find min/max o(1),
delete min/max o(log n)



Create a max heap from the given array (costing O(n) ). 
Keep removing the max of the heap K times. 
Now cost of finding max from the heap is O(1) but each time when max is removed,
we will have to run heapify and will cost O(logn). 
Now what if K = N(Number of elements in the heap).
Our total cost will be O(n) + O(nlogn)

For better solution refer to CLRS chapter9: Medians and Order Statistics

"""
import math


def build_max_heap(arr, index):

    largest = index

    left = index*2+1
    right = index*2+2

    array_size = len(arr)

    if left < array_size and arr[left] > arr[largest]:
        largest = left

    if right < array_size and arr[right] > arr[largest]:
        largest = right

    if largest != index:
        # swapping
        arr[largest], arr[index] = arr[index], arr[largest]
        build_max_heap(arr, largest)


def extract_max(arr):

    ret = arr[0]
    del arr[0]
    build_max_heap(arr, 0)
    return ret


if __name__ == "__main__":

    arr = [1, 2, 3, 4, 5, 6, 7]

    array_len = len(arr)

    """
    Heapify procedure can be applied to a node only if its children nodes are 
    heapified. So the heapification must be performed in the bottom up order.

    """

    for i in range(array_len//2, -1, -1):
        print(i)
        build_max_heap(arr, i)

    print("Max heap array {}".format(arr))

    # 3rd largest
    k_th = 3

    for i in range(k_th):
        val = extract_max(arr)

    print(" {} th largest element is = {}".format(k_th,val))
