package easy.removeduplicatesfromsortedarray;

/**
 *	Remove Duplicates from Sorted Array
 *  https://leetcode.com/problems/remove-duplicates-from-sorted-array
 */
class Solution {
    public int removeDuplicates(int[] nums) {
        // 중복 갯수
        int duplicatedCount = 0;

        // bubble sorting을 진행하는데 중복값의 경우는 최대값으로 설정한다.
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                // 중복값일 경우 최대값을 주어 맨 뒤로 보낸다.
                if (nums[i] != Integer.MAX_VALUE && nums[i] == nums[j]) {
                    nums[j] = Integer.MAX_VALUE;
                    duplicatedCount += 1;
                }

                if (nums[i] > nums[j]) {
                    int temp = nums[i];
                    nums[i] = nums[j];
                    nums[j] = temp;
                }
            }
        }

        // 유효한 범위의 index를 반환한다.
        return nums.length - duplicatedCount;
    }
}