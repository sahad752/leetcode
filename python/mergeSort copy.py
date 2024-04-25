
import sys



def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = mergeSort(left)
    right = mergeSort(right)

    return sort_partition(left, right)



def sort_partition(left, right):
    sorted_list = []
    len_a = len(left)
    len_b = len(right)

    i = j = 0

    while i < len_a and j < len_b:
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    while i < len_a:
        sorted_list.append(left[i])
        i += 1
    while j < len_b:
        sorted_list.append(right[j])
        j += 1

    return sorted_list

if __name__ == "__main__":
    elements = [2, 3, 10, 4, 5, 6, 9, 8, 7, 1]
    print(f"Unsorted elements: {elements}")
    sorted_elements = mergeSort(elements)
    print(f"Sorted elements: {sorted_elements}")
    sys.exit()