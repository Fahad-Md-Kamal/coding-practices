class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = {}
        for w in strs:
            sorted_w = "".join(sorted(w))
            if sorted_w not in res:
                res[sorted_w] = []
            res[sorted_w].append(w)
        
        return list(res.values())