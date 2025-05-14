package easy.removeelement;

/**
 * Remove Element
 * https://leetcode.com/problems/remove-element
 */
public class Solution {
	public int removeElement(int[] nums, int val) {
		// 유효한 index
		int validIndex = 0;

		for (int i = 0; i < nums.length; i++) {
			// i번째 값이 주어진 값과 다를 경우 유효한 index 위치에 해당 값을 할당한다.
			if (nums[i] != val) {
				nums[validIndex] = nums[i];
				validIndex++;
			}
		}

		return validIndex;
	}
}
