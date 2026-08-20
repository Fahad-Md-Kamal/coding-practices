class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        tmp = dict()
        for c in s:
            tmp[c] = tmp.get(c, 0) + 1

        for c in t:
            val = tmp.get(c, 0)
            if val <= 0:
                return False
            tmp[c] = val - 1
        return True
