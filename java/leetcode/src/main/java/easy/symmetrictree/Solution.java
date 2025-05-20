package easy.symmetrictree;

/**
 * Symmetric Tree
 * https://leetcode.com/problems/symmetric-tree
 */
public class Solution {
	public boolean isSymmetric(TreeNode root) {
		// 전달받은 노드가 null일 경우 true를 반환한다.
		if (root == null) {
			return true;
		}

		return this.symmetricHelper(root.left, root.right);
	}

	/**
	 * 대칭 여부 검사 helper 함수
	 * @param left 좌측 노드
	 * @param right 우측 노드
	 * @return 대칭 여부
	 */
	private boolean symmetricHelper(TreeNode left, TreeNode right) {
		// 좌측, 우측 모두 null일 경우 true를 반환한다.
		if (left == null && right == null) {
			return true;
		}

		// 둘 중 하나가 null일 경우 false를 반환한다.
		if (left == null || right == null) {
			return false;
		}

		/*
		 * 1. 좌측, 우측의 값이 같고
		 * 2. 좌측의 좌측, 우측의 우측을 검사한 결과
		 * 3. 좌측의 우측, 우측의 좌측을 검사한 결과
		 * 가 모두 일치할 경우 true를 반환한다.
		 */
		return (left.val == right.val) && this.symmetricHelper(left.left, right.right) && this.symmetricHelper(left.right, right.left);
	}
}
