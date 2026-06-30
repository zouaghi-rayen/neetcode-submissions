class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        existing_nums = []
        for num in nums:
            if num in existing_nums:
                return True
            else:
                existing_nums.append(num)
        return False