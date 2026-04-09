package silver;

import java.io.BufferedReader;
import java.io.InputStreamReader;

/**
 * 1463 1로 만들기
 * https://www.acmicpc.net/problem/1463
 */
public class P1463 {
    public static void run() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int x = Integer.parseInt(br.readLine());

        int[] dp = new int[x+1];
        dp[1] = 0;

        for (int i = 2; i < x + 1; i++) {
            dp[i] = dp[i - 1] + 1;

            if (i % 2 == 0) {
                dp[i] = Math.min(dp[i], dp[i / 2] + 1);
            }

            if (i % 3 == 0) {
                dp[i] = Math.min(dp[i], dp[i / 3] + 1);
            }
        }

        System.out.println(dp[x]);
    }
}
