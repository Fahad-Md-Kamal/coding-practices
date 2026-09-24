class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        tmpDict = dict()
        for n in nums:
            tmpDict[n] = tmpDict.get(n, 0) + 1
        
        bucket = [[] for _ in range(len(nums) + 1)]
        for key, val in tmpDict.items():
            bucket[val].append(key)
        
        result = []
        for i in range(len(bucket)-1, -1, -1):
            result = result + bucket[i]
            if len(result) >= k:
                return result[:k]
        return result
