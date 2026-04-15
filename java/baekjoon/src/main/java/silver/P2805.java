package silver;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 2805 나무 자르기
 * https://www.acmicpc.net/problem/2805
 */
public class P2805 {
    public static void run() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        long m = Long.parseLong(st.nextToken());
        long[] trees = new long[n];

        long left = 0;
        long right = 0;

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            trees[i] = Integer.parseInt(st.nextToken());
            right = Math.max(right, trees[i]);
        }

        long result = 0;
        while (left <= right) {
            long mid = (left + right) / 2;
            long remain = 0;

            for (int i = 0; i < n; i++) {
                if (mid >= trees[i]) {
                    continue;
                }
                remain += (trees[i] - mid);
            }

            if (remain >= m) {
                result = Math.max(result, mid);
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        System.out.println(result);
    }
}
