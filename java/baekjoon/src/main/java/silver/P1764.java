package silver;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

/**
 * 1764 듣보잡
 * https://www.acmicpc.net/problem/1764
 */
public class P1764 {
    public static void run() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        // 듣도 못한 사람 수
        int n = Integer.parseInt(st.nextToken());
        // 보도 못한 사람 수
        int m = Integer.parseInt(st.nextToken());

        Map<String, Boolean> notHearMap = new HashMap<>();
        for (int i = 0; i < n; i++) {
            notHearMap.put(br.readLine(), false);
        }

        List<String> notHearNseeList = new ArrayList<>();

        for (int i = 0; i < m; i++) {
            String notSee = br.readLine();

            if (notHearMap.containsKey(notSee)) {
                notHearNseeList.add(notSee);
            }
        }

        // 사전순으로 출력한다니 정렬
        Collections.sort(notHearNseeList);

        System.out.println(notHearNseeList.size());
        for (String notHearNsee : notHearNseeList) {
            System.out.println(notHearNsee);
        }
    }
}
