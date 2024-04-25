
def binary_search(arr,target):
    start = 0
    end = len(arr)-1

    while start <= end:
        mid = (start + end)//2
        if arr[mid] == target:
            return mid
        else:
            print(arr[mid])
            if arr[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
    return -1

def sqrt(x):
    l,r = 0,x
    res = 0
    while l<=r:
        m = l+((r-l)//2)
        if m**2 < x:
            l = m+1
        elif m**2 > x:
            r = m-1

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9,10]
    long_arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    saf = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,34,56,89]
    target = 18
    print(binary_search(saf,target))

