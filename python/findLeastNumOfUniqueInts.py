

def findLeastNumOfUniqueInts(nums,k):
    hash_map = {}
    for num in nums:
        hash_map[num] = hash_map.get(num,0)+1
    sorted_dict = dict(sorted(hash_map.items(), key=lambda item: item[1]))
    count = 0
    for key,value in sorted_dict.items():
        if value <=k:
            count+=1
            k-=value
    keys_to_remove = list(sorted_dict.keys())[:count]  # Get the first three keys
    for key in keys_to_remove:
        del sorted_dict[key]
    return len(sorted_dict)




arr =[5,5,4]

findLeastNumOfUniqueInts(arr,2)