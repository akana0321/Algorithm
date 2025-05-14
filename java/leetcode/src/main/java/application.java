import easy.mergetwosortedlists.Solution;
import easy.mergetwosortedlists.ListNode;

public class application {
    public static void main(String[] args) {
        Solution solution = new Solution();

        ListNode list1 = new ListNode(
                1,
                new ListNode(
                        2,
                        new ListNode(4)
                )
        );
        ListNode list2 = new ListNode(
                1,
                new ListNode(
                        3,
                        new ListNode(4)
                )
        );

        ListNode result = solution.mergeTwoLists(list1, list2);

        while (result != null) {
            System.out.println(result.val);
            result = result.next;
        }
    }
}
