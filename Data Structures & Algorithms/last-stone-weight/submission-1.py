class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort(reverse=True)
            x = stones[0]
            y = stones[1]
            if x == y:
                stones.pop(0)
                stones.pop(0)
                continue
            stones[1] = x - y
            stones.pop(0)

        if not stones:
            return 0
        return stones[0]
        