from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Create a map, on each insert into map, if already there, return false
        num_counts = {}
        for num in nums:
            if num in num_counts:
                return True 
            if num not in num_counts:
                num_counts[num] = 0
            num_counts[num] += 1
        return False 