class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue
            lp, rp = i+1, len(nums)-1
            while lp < rp:
                thSum = n + nums[lp] + nums[rp]
                if thSum < 0:
                    lp += 1
                elif thSum > 0:
                    rp -= 1
                else:
                    res.append([n, nums[lp], nums[rp]])
                    lp += 1
                    while nums[lp] == nums[lp-1] and lp < rp:
                        lp += 1
        return res