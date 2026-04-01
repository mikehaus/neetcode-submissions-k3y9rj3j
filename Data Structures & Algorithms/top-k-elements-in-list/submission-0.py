class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)

        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        return [num for num, _ in sorted_items[:k]]