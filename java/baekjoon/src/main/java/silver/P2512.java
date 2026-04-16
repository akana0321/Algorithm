package silver;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 2512 예산
 * https://www.acmicpc.net/problem/2512
 */
public class P2512 {
    public static void run() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] region = new int[n];
        long left = 0;
        long right = 0;

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            region[i] = Integer.parseInt(st.nextToken());
            right = Math.max(right, region[i]);
        }

        long budget = Long.parseLong(br.readLine());

        long result = 0;
        while (left <= right) {
            long mid = (left + right) / 2;

            long total = 0;
            for (int i = 0; i < n; i++) {
                total += Math.min((long) region[i], mid);
            }

            if (budget >= total) {
                left = mid + 1;
                result = mid;
            } else {
                right = mid - 1;
            }
        }

        System.out.println(result);
    }
}
