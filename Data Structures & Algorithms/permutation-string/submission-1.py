class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = ''.join(sorted(s1))
        
        l, r = 0, len(s1)
        while r < len(s2) + 1:
            sub = s2[l:r]
            sub = ''.join(sorted(sub))
            if sub == s1:
                return True
            l += 1
            r += 1

        return False