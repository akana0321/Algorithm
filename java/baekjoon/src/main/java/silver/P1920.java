package silver;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class P1920 {
    public static void run() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        Set<Integer> sourceSet = new HashSet<>();
        for (int i = 0; i < n; i++) {
            sourceSet.add(Integer.parseInt(st.nextToken()));
        }

        int m = Integer.parseInt(br.readLine());
        StringTokenizer st2 = new StringTokenizer(br.readLine());

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < m; i++) {
            int target = Integer.parseInt(st2.nextToken());
            sb.append(sourceSet.contains(target) ? 1 : 0).append('\n');
        }

        System.out.print(sb);
    }
}
