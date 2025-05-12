package easy.removeduplicatesfromsortedarray;

/**
 *	Remove Duplicates from Sorted Array
 *  https://leetcode.com/problems/remove-duplicates-from-sorted-array
 */
class Solution {
	public int removeDuplicates(int[] nums) {
		// 현재 유효한 index
		int validIndex = 0;
		for (int i = 0; i < nums.length; i++) {
			// 현재 유효한 index의 있는 값과 i번째에 있는 값이 다를 경우
			if (nums[i] != nums[validIndex]) {
				// 유효한 index를 하나 늘린다.
				// validIndex++;
				// 해당 값을 증가한 유효한 index 위치에 담는다.
				nums[++validIndex] = nums[i];
			}
		}

		// 길이를 반환해야 하므로 1을 더한다.
		return validIndex + 1;
	}
}