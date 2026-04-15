package gold;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

/**
 * 1931 회의실 배정
 * https://www.acmicpc.net/problem/1931
 */
public class P1931 {
    public static void run() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        List<int[]> timetable = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());

            timetable.add(new int[]{start, end});
        }

        // 종료시각 -> 시작시각 순으로 정렬
        timetable.sort((a, b) -> {
            if (a[1] == b[1]) {
                return a[0] - b[0];
            }
            return a[1] - b[1];
        });        

        int result = 0;
        int lastEnd = 0;

        for (int[] time : timetable) {
            // 시작시각이 직전 종료시각과 같거나 큰 경우 포함
            if (time[0] >= lastEnd) {
                result++;
                lastEnd = time[1];
            }
        }

        System.out.println(result);
    }
}
