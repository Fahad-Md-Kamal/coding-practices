class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        tmp_dict = dict()
        for ch in s:
            tmp_dict[ch] = tmp_dict.get(ch, 0) + 1
        
        for ch in t:
            val = tmp_dict.get(ch, 0)
            if val <= 0:
                return False
            tmp_dict[ch] = val - 1
        return sum(tmp_dict.values()) == 0
            