package easy.sametree;

/**
 * Same Tree
 * https://leetcode.com/problems/same-tree
 */
public class Solution {
	public boolean isSameTree(TreeNode p, TreeNode q) {
		// 두 노드가 모두 null일 경우 true를 반환한다.
		if (p == null && q == null) {
			return true;
		}

		// 두 노드 중 하나가 null일 경우 false를 반환한다.
		if (p == null || q == null) {
			return false;
		}

		// 두 노드의 값이 다를 경우 false를 반환한다.
		if (p.val != q.val) {
			return false;
		}

		// 두 노드의 좌측과 우측을 재귀적으로 확인한다.
		return this.isSameTree(p.left, q.left) && this.isSameTree(p.right, q.right);
	}
}
