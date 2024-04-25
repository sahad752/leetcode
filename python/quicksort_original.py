import sys


def swap(a,b,arr):
    if a!=b:
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp

def partition(elements,start,end):
    pivot_index = start
    pivot = elements[pivot_index]

    while start<end:
        while start<len(elements) and  elements[start] <= pivot:
            start+=1
        while elements[end]>pivot:
            end-=1
        if start < end:
            swap(start,end,elements)

    swap(pivot_index,end,elements)
    return end

def quicksort(elements,start,end):
    if start < end :
        pivot = partition(elements,start,end)
        quicksort(elements,start,pivot-1)
        quicksort(elements,pivot+1,end)
    return elements


if __name__ == "__main__":
    elements = [2, 3, 10, 4, 5, 6, 9, 8, 7, 1,3,5,7,2,5,63,4,6,24,6457,34,2,7657,24,46,84,2,658,452,23,5,86,35,46]
    print(f"Unsorted elements: {elements}")
    start = 0
    end = len(elements)-1
    sorted_elements = quicksort(elements,start,end)
    print(f"Sorted elements: {sorted_elements}")
    sys.exit()