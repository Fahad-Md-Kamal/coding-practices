class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmp = dict()
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in tmp:
                return [tmp[comp], i]
            tmp[nums[i]] = i
        return [-1, -1]