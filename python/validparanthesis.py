def isvalid(str):
    hashset = {}
    for s in str:
        hashset[s] = hashset.get(s,0)+1


    print(hashset)






if __name__ == "__main__":
    return_value = isvalid("(([]))")
    print(return_value)