package easy.binarytreeinordertraversal;

import java.util.ArrayList;
import java.util.List;

/**
 * Binary Tree Inorder Traversal
 * https://leetcode.com/problems/binary-tree-inorder-traversal
 */
public class Solution {
	public List<Integer> inorderTraversal(TreeNode root) {
		List<Integer> result = new ArrayList<>();

		// 전달받은 TreeNode가 없으면 빈 리스트를 반환한다.
		if (root == null) {
			return result;
		}

		// 중위순회한다.
		this.inorderHeler(root, result);

		return result;
	}

	private void inorderHeler(TreeNode treeNode, List<Integer> result) {
		// TreeNode의 좌측에 값이 있을 경우 없을 때까지 접근한다.
		if (treeNode.left != null) {
			this.inorderHeler(treeNode.left, result);
		}

		// TreeNode 좌측에 값이 있을 경우 담는다.
		result.add(treeNode.val);

		// TreeNode 우측에 값이 없을 때까지 접근한다.
		if (treeNode.right != null) {
			this.inorderHeler(treeNode.right, result);
		}
	}
}


