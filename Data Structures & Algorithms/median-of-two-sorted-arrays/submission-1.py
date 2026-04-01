class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        medianI = (len(nums1) + len(nums2)) // 2
        useTwo = (len(nums1) + len(nums2)) % 2 == 0

        heap = []
        for num in nums1:
            heapq.heappush(heap, num)
        for num in nums2:
            heapq.heappush(heap, num)
        
        to = medianI - 1 if useTwo else medianI
        for i in range(to):
            heapq.heappop(heap)
        if useTwo:
            l = heapq.heappop(heap)
            r = heapq.heappop(heap)
            return (l + r) / 2
        else:
            return heapq.heappop(heap)