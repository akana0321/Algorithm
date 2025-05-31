package easy.minimumdepthofbinarytree;

import easy.utill.TreeNode;

import java.util.LinkedList;
import java.util.Queue;

/**
 * Minimum Depth of Binary Tree
 * https://leetcode.com/problems/minimum-depth-of-binary-tree
 */
class Solution {
	public int minDepth(TreeNode root) {
		// 전달 받은 노드가 null일 경우 깊이가 0이므로 0을 반환한다.
		if (root == null) {
			return 0;
		}

		Queue<TreeNode> queue = new LinkedList<>();
		queue.offer(root);
		int depth = 1;

		// 큐가 비어 있지 않은 동안 반복한다.
		while (!queue.isEmpty()) {
			// 현재 깊이의 노드 개수
			int size = queue.size();

			// 현재 깊이(level)의 모든 노드를 하나씩 처리한다.
			for (int i = 0; i < size; i++) {
				TreeNode node = queue.poll();

				// 좌, 우 모두가 null일 경우 현재 깊이가 최소 깊이이므로 바로 반환한다.
				if (node.left == null && node.right == null) {
					return depth;
				}

				// 자식 노드가 존재하면 큐에 담아 다음 레벨에서 탐색
				if (node.left != null) {
					queue.offer(node.left);
				}

				if (node.right != null) {
					queue.offer(node.right);
				}
			}

			// 현재 레벨의 노드를 다 처리했으니 깊이 증가
			depth++;
		}

		return depth;
	}
}