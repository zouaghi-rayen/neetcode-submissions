class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements = dict()
        for num in nums:
            elements[num] = nums.count(num)
        return list(dict(heapq.nlargest(k, elements.items(), key=lambda item: item[1])).keys())
        
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        # Create an array of empty lists for frequencies from 0 to len(nums)
        freq = [[] for i in range(len(nums) + 1)]
        
        # Populate the buckets: index is the frequency, value is the number
        for num, frequency in count.items():
            freq[frequency].append(num)

            
        result = []
        
        # Iterate backwards from the highest frequency bucket to the lowest
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result