package silver;

import java.io.BufferedReader;
import java.io.InputStreamReader;

/**
 * 9095 1, 2, 3 더하기
 * https://www.acmicpc.net/problem/9095
 */
public class P9095 {
    public static void run() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());
        int[] ns = new int[t];

        for (int i = 0; i < t; i++) {
            ns[i] = Integer.parseInt(br.readLine());
        }

        StringBuilder sb = new StringBuilder();
        for (int n : ns) {
            sb.append(getOneTwoThress(n)).append("\n");
        }

        System.out.println(sb);
    }

    public static int getOneTwoThress(int target) {
        if (target == 1) {
            return 1;
        }

        if (target == 2) {
            return 2;
        }

        if  (target == 3) {
            return 4;
        }

        int[] dp = new int[target + 1];
        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 4;

        for (int i = 4; i <= target; i++) {
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
        }

        return dp[target];
    }
}
