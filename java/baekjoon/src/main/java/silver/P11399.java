package silver;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

/**
 * 11399 ATM
 * https://www.acmicpc.net/problem/11399
 */
public class P11399 {
    public static void run() throws Exception {
        int result = 0;

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[] turnaround = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            turnaround[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(turnaround);

        for (int i = 0; i < n; i++) {
            result += (turnaround[i] * (n - i));
        }

        System.out.println(result);
    }
}
