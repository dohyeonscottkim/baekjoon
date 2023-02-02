n = int(input())

array = []

for i in range(n):
    array.append(int(input()))
    

# https://modulabs.co.kr/blog/algorithm-python/

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
def quicksort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]
    
    left = [i for i in tail if i <= pivot]
    right = [i for i in tail if i > pivot]
    
    return quicksort(left) + [pivot] + quicksort(right)

array = quicksort(array)

for i in range(n):
    print(array[i])

#merge sort(병합 정렬)

#heap sort(힙 정렬)

#radix sort(기수 정렬)

#count sort(계수 정렬)