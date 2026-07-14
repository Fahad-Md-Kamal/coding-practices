class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tmp_set = set()
        for n in nums:
            if n in tmp_set:
                return True
            tmp_set.add(n)
        return False