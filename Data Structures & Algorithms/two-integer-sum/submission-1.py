class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmpDict = dict()
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in tmpDict:
                return [tmpDict[comp], i]
            tmpDict[nums[i]] = i
        return [-1, -1]
