class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tmp = {}
        for w in strs:
            ord_w = "".join(sorted(w))
            if ord_w not in tmp:
                tmp[ord_w] = []
            tmp[ord_w].append(w)
        return list(tmp.values())