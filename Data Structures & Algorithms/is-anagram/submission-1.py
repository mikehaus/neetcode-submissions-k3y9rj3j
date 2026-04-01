class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sSorted = "".join(sorted(s))
        tSorted = "".join(sorted(t))

        return sSorted == tSorted 