package easy.searchinsertposition;

/**
 * Search Insert Position
 * https://leetcode.com/problems/search-insert-position
 */
public class Solution {
	public int searchInsert(int[] nums, int target) {
		// 왼쪽
		int left = 0;
		// 오른쪽
		int right = nums.length - 1;

		// 왼쪽이 오른쪽과 크거나 같아질 때까지 반복한다.
		while (left <= right) {
			// 중간 지점을 구한다.
			int mid = left + (right - left) / 2;

			if (nums[mid] == target) {
				// 중간값이 목표값과 같을 경우 중간 지점을 반환한다.
				return mid;
			} else if (nums[mid] > target) {
				// 중간값이 목표값보다 클 경우 오른쪽을 한 칸 뒤로 옮긴다.
				right = mid - 1;
			} else {
				// 중간값이 목표값보다 작을경우 왼쪽을 한 칸 앞으로 옮긴다.
				left = mid + 1;
			}
		}

		// 왼쪽을 반환한다.
		return left;
	}
}
