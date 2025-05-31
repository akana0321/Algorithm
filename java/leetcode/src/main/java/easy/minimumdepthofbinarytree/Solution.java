package easy.minimumdepthofbinarytree;

import easy.utill.TreeNode;

/**
 * Minimum Depth of Binary Tree
 * https://leetcode.com/problems/minimum-depth-of-binary-tree
 */
class Solution {
	public int minDepth(TreeNode root) {
		if (root == null) {
			return 0;
		}

		int left = minDepth(root.left);
		int right = minDepth(root.right);

		// 한쪽 자식만 존재하는 경우 → 존재하는 쪽으로 깊이 계산
		if (left == 0 || right == 0) {
			return left + right + 1;
		}

		// 양쪽 자식 모두 존재하는 경우 → 더 얕은 쪽 선택
		return Math.min(left, right) + 1;
	}
}