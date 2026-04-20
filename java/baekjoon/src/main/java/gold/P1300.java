package gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 1300 K번째 수 - 실패
 * https://www.acmicpc.net/problem/1300
 */
public class P1300 {
    public static void run() throws IOException {
        long result = 0;

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int k = Integer.parseInt(br.readLine());

        // 첫번째부터
        long left = 1;
        // k번째까지
        long right = k;

        while (left <= right) {
            long mid = (left + right) / 2;

            long count = 0;
            for (int i = 1; i <= n; i++) {
                count += Math.min(n, mid / i);
            }

            if (count >= k) {
                result = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        System.out.println(result);
    }
}
