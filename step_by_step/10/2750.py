n = int(input())

array = []

for i in range(n):
    array.append(int(input()))

#selection sort(선택정렬)) o(n^2)
# for i in range(n):
#     minIndex = i
#     for j in range(i+1, n):
#         if array[minIndex] > array[j]:
#             minIndex = j
#     array[i], array[minIndex] = array[minIndex], array[i]
    
# for i in range(n):
#     print(array[i])
    
#insertion sort(삽입정렬) o(n^2)
# for i in range(1, n):
#     for j in range(i, 0, -1):
#         if array[j-1] > array[j]:
#             array[j-1], array[j] = array[j], array[j-1]
#         else:
#             break
        
# for i in range(n):
#     print(array[i])

#bubble sort(버블정랼) o(n^2)
# for i in range(n):
#     for j in range(n-i-1):
#         if array[j] > array[j+1]:
#             array[j], array[j+1] = array[j+1], array[j]

# for i in range(n):
#     print(array[i])
        
#quick sort(퀵정렬) average:o(nlogn) worst: o(n^2)
#quick sort - conventional method
# def quicksort(array, start, end):
#     if start >= end:
#         return
    
#     pivot = start
#     left = start+1
#     right = end
    
#     while left <= right:
        
#         while left <= end and array[left] <= array[pivot]:
#             left += 1
        
#         while right > start and array[right] >= array[pivot]:
#             right -= 1
        
#         if left > right:
#             array[right], array[pivot] = array[pivot], array[right]
#         else:
#             array[left], array[right] = array[right], arrya[left]
    
#     quicksort(array, start, right-1)
#     quicksort(array, right+1, end)

#quicksort - pythonic method
# def quicksort(array):
#     if len(array) <= 1:
#         return array
    
#     pivot = array[0]
#     tail = array[1:]
    
#     left = [i for i in tail if i <= pivot]
#     right = [i for i in tail if i > pivot]
    
#     return quicksort(left) + [pivot] + quicksort(right)

# array = quicksort(array)

# for i in range(n):
#     print(array[i])

#merge sort(병합 정렬)
# def mergeSort(array:list):
#     if len(array) > 1:
#         leftArray = array[:len(array)//2]
#         rightArray = array[len(array)//2:]
        
#         mergeSort(leftArray)
#         mergeSort(rightArray)
        
#         l = 0
#         r = 0
#         m = 0
        
#         while l < len(leftArray) and r < len(rightArray):
#             if leftArray[l] < rightArray[r]:
#                 array[m] = leftArray[l]
#                 l += 1
#             else:
#                 array[m] = rightArray[r]
#                 r += 1
#             m += 1
        
#         while l < len(leftArray):
#             array[m] = leftArray[l]
#             l += 1
#             m += 1
        
#         while r < len(rightArray):
#             array[m] = rightArray[r]
#             r += 1
#             m += 1
            
# mergeSort(array)

# for i in range(n):
#     print(array[i])

#heap sort(힙 정렬)
# def heapify(arr, idx, size):
#     left = idx*2
#     right = idx*2 + 1
#     largest = idx
    
#     if left < size and arr[left] > arr[largest]:
#         largest = left
    
#     if right < size and arr[right] > arr[largest]:
#         largest = right
    
#     if largest != idx:
#         arr[idx], arr[largest] = arr[largest], arr[idx]
#         heapify(arr, largest, size)
        
# def heapsort(arr):
#     size = len(arr)
    
#     for i in range(size//2-1, -1, -1):
#         heapify(arr, i, size)
    
#     for i in range(n-1, 0, -1):
#         arr[0], arr[i] = arr[i], arr[0]
#         heapify(arr, 0, i)
    
#     return arr

# sortedArray = heapsort(array)
# 
# for i in range(n):
#     print(sortedArray[i])

#radix sort(기수 정렬)
# def countingSort(arr, digit):
#     n = len(arr)
    
#     output = [0 for i in range(n)]
#     count = [0 for i in range(10)]
    
#     for i in range(n):
#         index = arr[i] // digit
#         count[index % 10] += 1
    
#     for i in range(1, 10):
#         count[i] += count[i-1]
    
#     i = n-1

#     while i >= 0:
#         index = arr[i] // digit
#         output[count[index % 10]-1] = arr[i]
#         count[index%10] -= 1
#         i -= 1
    
#     for i in range(n):
#         arr[i] = output[i]

# def radixSort(arr):
#     max_element = max(arr)
    
#     digit = 1
    
#     while max_element // digit > 0:
#         countingSort(arr, digit)
#         digit *= 10
    
# radixSort(array)

# for i in range(n):
#     print(array[i])
    
#count sort(계수 정렬)
def countingSort(arr):
    n = len(arr)
    max_element = max(arr)
    
    output = [0 for i in range(n)]
    count = [0 for i in range(max_element+1)]
    
    for i in range(n):
        count[arr[i]] += 1
        
    for i in range(1, max_element+1):
        count[i] += count[i-1]
        
    i = n-1

    while i >= 0:
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1
        
    for i in range(n):
        arr[i] = output[i]
    
countingSort(array)

for i in range(n):
    print(array[i])
    