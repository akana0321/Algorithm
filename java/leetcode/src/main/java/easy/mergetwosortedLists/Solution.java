package easy.mergetwosortedlists;

/**
 * Merge Two Sorted Lists
 * https://leetcode.com/problems/merge-two-sorted-lists/
 */
public class Solution {
	public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
		if (list1 == null && list2 == null) {
			// 전달받은 노드가 모두 null일 경우 null 반환
			return null;
		} else if (list1 != null && list2 == null) {
			// list2가 null일 경우 list1 반환
			return list1;
		} else if (list1 == null && list2 != null) {
			// list1이 null일 경우 list2 반환
			return list2;
		} else {
			// 결과를 담을 노드 선언 - 가장 앞에 두기 위해 최저값을 준다.
			ListNode result = new ListNode(Integer.MIN_VALUE);
			// 현재 노드
			ListNode current = result;

			// 전달받은 두 노드 중 하나가 null이 될 때까지 순회한다.
			while (list1 != null && list2 != null) {
				if (list1.val <= list2.val) {
					current.next = list1;
					list1 = list1.next;
				} else {
					current.next = list2;
					list2 = list2.next;
				}

				// 현재 노드를 다음으로 넘어간다.
				current = current.next;
			}

			// 남은 노드를 현재 노드의 다음으로 지정한다.
			current.next = list1 == null ? list2 : list1;

			return result.next;
		}
	}

	/**
	 * 확인용 리스트 노드 로그
	 * @param ln
	 */
	private void logListNode(ListNode ln) {
		String str = "[ ";

		while(ln != null) {
				str += (ln.val + ", ");
				ln = ln.next;
		}

		str += " ]";

		System.out.println(str);
	}
}
