
def romantoint(s):
        m = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        ans = m[s[len(s)-1]]

        for i in range(len(s)-2 ,-1,-1):
            if m[s[i]] < m[s[i+1]]:
                ans-=m[s[i]]
            else:
                ans+=m[s[i]]
        print(ans)

if __name__ == "__main__":
    romantoint("VXII")