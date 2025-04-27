import easy.twosum.Solution;

public class application {
    public static void main(String[] args) {
        Solution solution = new Solution();

        int[] result = solution.twoSum(new int[]{3,2,4}, 6);

        System.out.println("[" + result[0] + ", " + result[1] + "]");
    }
}
