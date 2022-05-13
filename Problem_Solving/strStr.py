class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if len(needle) == 0:
            return 0

        if not needle in haystack:
            return -1

        while len(haystack) >= 1 and len(needle) <= 104:         # Constraints
            haystack, needle = haystack.lower(), needle.lower()  # Constraints
            return haystack.index(needle)


inst = Solution()
print(inst.strStr("hello", "ll"))  # returns the first occurence (2)
print(inst.strStr("www", "ll"))   # returns -1 (-1)
print(inst.strStr("www", ""))     # returns 0  (0)
