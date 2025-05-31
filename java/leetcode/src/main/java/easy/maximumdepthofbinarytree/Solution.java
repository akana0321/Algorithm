package easy.maximumdepthofbinarytree;

/**
 * Maximum Depth of Binary Tree
 * https://leetcode.com/problems/maximum-depth-of-binary-tree
 */
class Solution {
	public int maxDepth(TreeNode root) {
		int result = 0;

		// 전달받은 노드가 null이면 0을 반환한다.
		if (root == null) {
			return result;
		}

		// 왼쪽의 깊이를 구한다.
		int leftDepth = maxDepth(root.left);

		// 오른쪽의 깊이를 구한다.
		int rightDepth = maxDepth(root.right);

		// 왼쪽과 오른쪽 중 큰 값 + 1(전달받은 TreeNode)
		result = Math.max(leftDepth, rightDepth) + 1;

		return result;
	}
}