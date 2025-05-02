import easy.longestcommonprefix.Solution;

public class application {
    public static void main(String[] args) {
        Solution solution = new Solution();

        String result = solution.longestCommonPrefix(new String[] { "flower","flow","flight" });

        System.out.println(result);
    }
}
