class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([f"{len(wrd)}#{wrd}" for wrd in strs])

    def decode(self, s: str) -> List[str]:
        res = []
        l = 0
        while l < len(s):
            r = l
            while r < len(s) and s[r] != "#":
                r += 1
            length = int(s[l:r])
            l = r + 1
            res.append(s[l:l+length])
            l = l + length
        return res
