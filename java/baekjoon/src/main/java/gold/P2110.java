package gold;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

/**
 * 2110 공유기 설치
 * https://www.acmicpc.net/problem/2110
 */
public class P2110 {
    public static void run() throws Exception {
        long result = 0;

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int c =  Integer.parseInt(st.nextToken());

        int[] x = new int[n];
        for (int i = 0; i < n; i++) {
            x[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(x);

        long left = 1;
        long right = x[n - 1] - x[0];

        while (left <= right) {
            long mid = (left + right) / 2;

            int count = 1;
            int next = x[0];

            for (int i = 0; i < n; i++) {
                if (x[i] - next >= mid) {
                    count++;
                    next = x[i];
                }
            }

            if (count >= c) {
                result = mid;
                left = mid + 1;
            } else {
                right  = mid - 1;
            }
        }

        System.out.println(result);
    }
}
