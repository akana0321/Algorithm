package silver;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 2559 수열
 * https://www.acmicpc.net/problem/2559
 */
public class P2559 {
    public static void run() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[] temperatures = new int[n + 1];
        st = new StringTokenizer(br.readLine());

        for (int i = 1; i <= n; i++) {
            temperatures[i] = Integer.parseInt(st.nextToken());
        }

        int kSum = 0;
        for (int i = 1; i <= k; i++) {
            kSum += temperatures[i];
        }

        int max = kSum;
        for (int i = k + 1; i <= n; i++) {
            kSum = kSum + temperatures[i] - temperatures[i - k];
            max = Math.max(max, kSum);
        }

        System.out.println(max);
    }
}
