package easy.twosum;

/**
 * tow sum
 * https://leetcode.com/problems/two-sum/description/?difficulty=EASY
 */
public class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[] { 0, 0 };

        for (int i = 0; i < nums.length - 1; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                int sum = nums[i] + nums[j];

                if (sum == target) {
                    return new int[] { i, j };
                }
            }
        }

        return result;
    }
}