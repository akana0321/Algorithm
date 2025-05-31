package easy.balancedbinarytree;

import easy.utill.TreeNode;

/**
 * Balanced Binary Tree
 * https://leetcode.com/problems/balanced-binary-tree
 */
public class Solution {
	public boolean isBalanced(TreeNode root) {
		// 높이가 -1(불균형)이 아닐 경우 균형
		return this.getHeight(root) != -1;
	}

	/**
	 * 전달 받은 노드의 좌, 우 높이를 반환하며 불균형일 경우 -1을 반환한다.
	 * @param node
	 * @return
	 */
	private int getHeight(TreeNode node) {
		// 전달받은 노드가 null이면 높이는 0
		if (node == null) {
			return 0;
		}

		// 좌, 우 길이를 구한다.
		int left = this.getHeight(node.left);
		int right = this.getHeight(node.right);

		// 둘 중 하나가 -1이면 불균형
		if (left == -1 || right == -1) {
			return -1;
		}

		// 현재 노드가 불균형이면 -1 반환
		if (Math.abs(left - right) > 1) {
			return -1;
		}

		// 정상 높이 반환
		return Math.max(left, right) + 1;
	}
}

