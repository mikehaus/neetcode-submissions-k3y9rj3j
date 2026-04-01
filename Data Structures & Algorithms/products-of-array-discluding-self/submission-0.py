from functools import reduce

class Solution:
    def product(self, x: int, y: int) -> int:
        return x * y

    def nonZero(self, x: int) -> bool:
        return x != 0

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        filtered = list(filter(self.nonZero, nums))
        total = reduce(self.product, filtered, 1)

        zero_count = nums.count(0)
        res = []

        if zero_count > 1:
            res = [0] * len(nums)
        elif zero_count == 1:
            for n in nums:
                if n == 0:
                    res.append(total)
                else:
                    res.append(0)
        else:
            for n in nums:
                res.append(total // n)
        return res