def longestcp(strd):
    temp = strd[0]
    ans = []

    if '' in strd:
        return ''

    for str in strd[1:]:
        for i in range(0,len(str)):
            if (i < len(temp)) and (temp[i] != str[i]):
                temp = temp[:i]
                break
            if len(str)<len(temp):
                temp = temp[:len(str)]

    return temp




if __name__ == "__main__":
    # stss = ["abab","aba",""]
    stss = ["ab","a"]

    ans = longestcp(stss)
    print("answer is ",ans)