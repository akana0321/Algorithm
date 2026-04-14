package silver;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 1149 RGB 거리
 * https://www.acmicpc.net/problem/1149
 */
public class P1149 {
    public static void run() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] house =  new int[n + 1][4];
        int[][] dp = new int[n + 1][4];

        for (int i = 1; i <= n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 1; j < 4; j++) {
                house[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i = 1; i <= n; i++) {
            dp[i][1] = Math.min(dp[i - 1][2], dp[i - 1][3]) + house[i][1];
            dp[i][2] = Math.min(dp[i - 1][1], dp[i - 1][3]) + house[i][2];
            dp[i][3] = Math.min(dp[i - 1][1], dp[i - 1][2]) + house[i][3];
        }

        int result = Math.min(dp[n][1], Math.min(dp[n][2], dp[n][3]));

        System.out.println(result);
    }
}
