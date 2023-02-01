n = int(input())

array = []

for i in range(n):
    array.append(int(input()))
    

# https://modulabs.co.kr/blog/algorithm-python/

# selection sort(선택정렬)) o(n^2)
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

#bubble sort(버블정랼)
for i in range(n):
    for j in range(n-i-1):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]

for i in range(n):
    print(array[i])
        
#quick sort(퀵정렬)

#merge sort(병합 정렬)

#heap sort(힙 정렬)

#radix sort(기수 정렬)

#count sort(계수 정렬)