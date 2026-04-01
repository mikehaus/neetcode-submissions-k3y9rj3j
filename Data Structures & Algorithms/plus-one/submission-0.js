class Solution {
    /**
     * @param {number[]} digits
     * @return {number[]}
     */
    plusOne(digits) {
        const sum = parseInt(digits.join('')) + 1;
        return sum.toString().split("");
    }
}
