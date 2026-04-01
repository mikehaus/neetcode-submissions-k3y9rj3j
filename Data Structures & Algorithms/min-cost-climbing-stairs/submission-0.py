class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def getCost(i):
            if i >= len(cost):
                return 0
            return cost[i] + min(getCost(i + 1), getCost(i + 2))

        return min(getCost(0), getCost(1))