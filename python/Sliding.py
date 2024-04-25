class Sliding:
    def needlehaystack(self,haystack,needle):
        if haystack == needle:
            return 0

        len_h = len(haystack)
        len_n = len(needle)

        for i in range(len_h - len_n +1):
            window = haystack[i:i+len_n]
            if window == needle:
                return i

        return -1

    def visualize_kmp(self,haystack, needle):
        len_haystack, len_needle = len(haystack), len(needle)

        # Build the KMP table
        kmp_table = [0] * len_needle
        j = 0

        print(f"Building KMP table for pattern '{needle}':")
        for i in range(1, len_needle):
            print(f"current i letter is {needle[i]}")
            print(f'current j letter is {needle[j]}')
            while j > 0 and needle[j] != needle[i]:
                j = kmp_table[j - 1]
            if needle[j] == needle[i]:
                j += 1
            kmp_table[i] = j
            print(f"Table: {kmp_table[:i+1]} and needle is {needle[:i+1]}")

        print("\nKMP Table:", kmp_table)

        # Perform the actual search using KMP
        j = 0
        print(f"\nSearching for pattern '{needle}' in text '{haystack}':")
        for i in range(len_haystack):
            while j > 0 and haystack[i] != needle[j]:
                j = kmp_table[j - 1]
            if haystack[i] == needle[j]:
                j += 1
            print(f"Comparing: {haystack[:i+1]} with {needle[:j]}")

            if j == len_needle:
                print(f"\nPattern found at index {i - len_needle + 1}\n")
                j = kmp_table[j - 1]

        print("\nPattern not found in the text.")




if __name__ == "__main__":
    s = Sliding()
    # Example usage
    haystack = "ABABDABACDABABCABABCAB"
    needle = "BCAB"
    result = s.visualize_kmp(haystack, needle)
    print(result)