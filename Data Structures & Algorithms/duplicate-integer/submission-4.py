class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tmp_dict = dict()
        for n in nums:
            if n in tmp_dict:
                return True
            tmp_dict[n] = 1
        return False