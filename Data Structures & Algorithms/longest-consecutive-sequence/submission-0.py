class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        mxSq = 0

        for i in seen:
            if (i - 1) not in seen:
                long = 1
                while (i + long) in seen:
                    long += 1
                mxSq = max(mxSq, long)
        return mxSq
