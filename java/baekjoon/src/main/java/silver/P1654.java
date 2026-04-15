package silver;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 1654 랜선 자르기
 * https://www.acmicpc.net/problem/1654
 */
public class P1654 {
    public static void run() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[] lans =  new int[n];
        long right = 0;
        for (int i = 0; i < n; i++) {
            lans[i] = Integer.parseInt(br.readLine());
            right =  Math.max(right, lans[i]);
        }

        long left = 1;
        while (left <= right) {
            long count = 0;
            long mid = (left + right) / 2;

            for  (int i = 0; i < n; i++) {
                count += (lans[i] / mid);
            }

            if (count >= k) {
                // 갯수가 주어진 수보다 많이 나온 경우
                left = mid + 1;
            } else {
                // 갯수가 주어진 수보다 덜 나온 경우
                right = mid - 1;
            }
        }

        System.out.println(right);
    }
}
