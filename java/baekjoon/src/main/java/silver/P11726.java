package silver;

import java.io.BufferedReader;
import java.io.InputStreamReader;

/**
 * 11726 2xn 타일링
 * https://www.acmicpc.net/problem/11726
 */
public class P11726 {
    public static void run() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n =  Integer.parseInt(br.readLine());

        if (n == 1) {
            System.out.println(1);
            return;
        }

        int[] dp = new int[n+1];
        dp[1] = 1;
        dp[2] = 2;

        for (int i = 3; i <= n; i++) {
            dp[i] = (dp[i - 1] + dp[i - 2]) % 10007;
        }

        System.out.println(dp[n]);
    }
}
