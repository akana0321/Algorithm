package easy.minimumdepthofbinarytree;

import easy.utill.TreeNode;

/**
 * Minimum Depth of Binary Tree
 * https://leetcode.com/problems/minimum-depth-of-binary-tree
 */
class Solution {
	public int minDepth(TreeNode root) {
		return this.getHeight(root);
	}

	public int getHeight(TreeNode node) {
		int height = 0;

		// 전달 받은 node가 null일 경우 높이는 0
		if (node == null) {
			return height;
		}

		// 좌, 우 높이를 구한다.
		int left = this.getHeight(node.left);
		int right = this.getHeight(node.right);

		// 한 쪽의 높이만 0일 경우는 아닌 쪽을, 둘 다 높이가 0이 아닐 경우는 작은 값을 준다.
		if (left == 0 && right != 0) {
			height = right;
		} else if (left != 0 && right == 0) {
			height = left;
		} else {
			height = Math.min(left, right);
		}

		// 1(현재 노드) + height를 반환한다.
		return 1 + height;
	}
}