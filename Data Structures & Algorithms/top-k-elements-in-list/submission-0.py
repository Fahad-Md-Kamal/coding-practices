class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        bucket = [[] for n in range(len(nums) + 1)]
        for key, val in freq.items():
            bucket[val].append(key)
        
        res = []
        for itm in range(len(bucket) -1, -1, -1):
            if bucket[itm] and len(res) < k:
                res += bucket[itm]
        return res