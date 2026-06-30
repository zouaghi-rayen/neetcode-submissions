class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements = dict()
        for num in nums:
            elements[num] = nums.count(num)
        return list(dict(heapq.nlargest(k, elements.items(), key=lambda item: item[1])).keys())
        
