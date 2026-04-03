package silver;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

/**
 * 숫자 카드
 * https://www.acmicpc.net/problem/10815
 */
public class P10815 {
    public static void run() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] sourceArray = new int[n];
        for (int i = 0; i < n; i++) {
            sourceArray[i] = Integer.parseInt(st.nextToken());
        }
        // 정렬 한 번 쳐줌
        Arrays.sort(sourceArray);

        int m = Integer.parseInt(br.readLine());
        StringTokenizer st2 = new StringTokenizer(br.readLine());
        int[] targetArray = new int[m];
        for (int i = 0 ; i < m; i++) {
            targetArray[i] = Integer.parseInt(st2.nextToken());
        }

        StringBuilder sb = new StringBuilder();

        for (int target : targetArray) {
            boolean result = isExist(sourceArray, target);
            sb.append(result ? "1" : "0").append(" ");
        }

        System.out.println(sb);
    }

    private static boolean isExist(int[] sourceArray, int target) {
        boolean result = false;

        int left = 0;
        int right = sourceArray.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (sourceArray[mid] == target) {
                result = true;
                break;
            } else if (sourceArray[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return result;
    }


}
