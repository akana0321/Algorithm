package easy.searchinsertposition;

/**
 * Search Insert Position
 * https://leetcode.com/problems/search-insert-position
 */
public class Solution {
	public int searchInsert(int[] nums, int target) {
		// 시작점을 임시로 전달받은 배열의 가운데로 잡는다.
		int startIndex = (nums.length - 1) / 2;
		// 만약 가운데 지점의 값이 목표값보다 크다면 처음부터 시작하게 한다.
		if (target < nums[startIndex]) {
			startIndex = 0;
		}

		for (int i = startIndex; i < nums.length; i++) {
			// 목표값이 배열의 i번째 값보다 작거나 같은 경우 i를 반환한다.
			if (target <= nums[i]) {
				return i;
			}
		}

		// 위의 반복문을 통과했을 경우 가장 뒤에 목표값을 추가하게 한다.
		return nums.length;
	}
}
