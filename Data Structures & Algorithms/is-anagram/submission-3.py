class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tmp_dict = dict()
        for ch in s:
            if ch in tmp_dict:
                tmp_dict[ch] = tmp_dict[ch] + 1
            else:
                tmp_dict[ch] = 1
        for ch in t:
            if ch not in tmp_dict or tmp_dict[ch] == 0:
                return False
            
            tmp_dict[ch] -= 1
        return sum(tmp_dict.values()) == 0
            
            