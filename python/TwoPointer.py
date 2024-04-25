class TwoPointer:
    def ispal(self,word):
        start = 0
        end = len(word)-1
        while start <= end and word[start] == word[end]:
            start+=1
            end=-1
        return start >= end



if __name__ == "__main__":
    twop = TwoPointer()
    print(twop.ispal("qqwerewqq"))