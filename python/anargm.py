from typing import Counter, List


def findAnargm(s,p)->List[int]:
    s_len = len(s)
    p_len = len(p)
    if s_len < p_len:
        return []

    p_count = Counter(p)
    s_count = Counter()
    result = []

    for i in range(s_len):
        s_count[s[i]]+=1
        if i>=p_len:
            if s_count[s[i-p_len]]==1:
                del s_count[s[i-p_len]]
            else:
                s_count[s[i-p_len]]-=1
        if s_count==p_count:
            result.append(i-p_len+1)

    print(result)

findAnargm("sdsasaas","saa")