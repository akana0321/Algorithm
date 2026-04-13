package silver;

import java.io.BufferedReader;
import java.io.InputStreamReader;

/**
 * 11727 2×n 타일링 2
 * https://www.acmicpc.net/problem/11727
 */
public class P11727 {
    public static void run() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n =  Integer.parseInt(br.readLine());

        if (n == 1) {
            System.out.println(1);
            return;
        }

        int[] dp = new int[n+1];
        dp[1] = 1;
        dp[2] = 3;

        for (int i = 3; i <= n; i++) {
            dp[i] = (dp[i - 1] + dp[i - 2] * 2) % 10007;
        }

        System.out.println(dp[n]);
    }
}
