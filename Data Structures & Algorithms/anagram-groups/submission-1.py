class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tmp_dict = {}
        for word in strs:
            freq = [0] * 26
            for ch in word:
                freq[ord(ch) - ord("a")] += 1
            key = tuple(freq)

            if key not in tmp_dict:
                tmp_dict[key] = []
            tmp_dict[key].append(word)
        return list(tmp_dict.values())