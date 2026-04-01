class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers, target) {
        let result = [-1, -1];
        let l = 0;
        let r = numbers.length - 1;

        while (l < r) {
            const left = numbers[l];
            const right = numbers[r];
            if (left + right == target) return [l + 1, r + 1];
            if (left + right >= target) r--;
            else if (left + right < target) l++;
        }
        return result;
    }
}
