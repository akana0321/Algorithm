package silver;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

/**
 * 2606 바이러스
 * https://www.acmicpc.net/problem/2606
 */
public class P2606 {
    public static void run() throws Exception {
        int result = 0;

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int computerCount = Integer.parseInt(br.readLine());
        // 컴퓨터 간 연결 관계를 담을 List
        List<Integer>[] computerGraph = new ArrayList[computerCount + 1];
        for (int i = 0; i < computerCount + 1; i++) {
            computerGraph[i] = new ArrayList<>();
        }

        int computerPairCount = Integer.parseInt(br.readLine());

        // 쌍이 없으면 0 출력 후 종료
         if (computerPairCount == 0) {
             System.out.println(result);
             return;
         }

        for (int i = 0; i < computerPairCount; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int cp1 = Integer.parseInt(st.nextToken());
            int cp2 = Integer.parseInt(st.nextToken());

            // 서로의 List에 담는다.
            computerGraph[cp1].add(cp2);
            computerGraph[cp2].add(cp1);
        }

        boolean[] visited = new boolean[computerCount + 1];

        result = deepFirstSearch(computerGraph, visited, 1) - 1;

        System.out.println(result);
    }

    private static int deepFirstSearch(List<Integer>[] graph, boolean[] visited, int start) {
        visited[start] = true;
        int count = 1;

        for (int next : graph[start]) {
            if (!visited[next]) {
                count += deepFirstSearch(graph, visited, next);
            }
        }

        return count;
    }
}
