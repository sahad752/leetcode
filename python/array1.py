





def uniqueOccurrences( nums):
    """
    :type arr: List[int]
    :rtype: bool
    """
    hash_map = {}
    for n in nums:
        hash_map[n] = hash_map.get(n,0)+1

    values = hash_map.values()
    unique_vvals = set(values)
    return len(unique_vvals) == len(hash_map)

if __name__ == "__main__":
    res = uniqueOccurrences([2,3,34,3,3,3,2,34,5,1,1,2,7,7,8,3])