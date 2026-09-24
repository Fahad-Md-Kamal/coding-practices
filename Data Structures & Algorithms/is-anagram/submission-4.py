class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        tmpDict = dict()

        for ch in s:
            tmpDict[ch] = tmpDict.get(ch, 0) + 1

        for ch in t:
            val = tmpDict.get(ch, 0)
            if val == 0:
                return False
            else:
                tmpDict[ch] = tmpDict.get(ch) - 1
        return sum(tmpDict.values()) == 0
