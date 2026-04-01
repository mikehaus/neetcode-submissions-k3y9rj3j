class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const map = new Map();
        for (let i = 0; i < nums.length; i++) {
            const num = nums[i];
            const complement = target - num;
            const sumIndex = map.get(complement);

            if (map.has(complement)) {
                return [i, sumIndex]
            }

            map.set(num, i)
        }

        return [-1, -1];
    }
}
