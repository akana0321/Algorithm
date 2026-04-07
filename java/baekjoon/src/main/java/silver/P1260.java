package silver;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

/**
 * 1260 DFS와 BFS
 * https://www.acmicpc.net/problem/1260
 */
public class P1260 {
    public static void run() throws Exception {
        StringBuilder sb =  new StringBuilder();

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st1 = new StringTokenizer(br.readLine());

        // 정점의 개수
        int n = Integer.parseInt(st1.nextToken());
        // 간선의 개수
        int m = Integer.parseInt(st1.nextToken());
        // 시작할 정점
        int k = Integer.parseInt(st1.nextToken());

        List<Integer>[] graph = new ArrayList[n + 1];
        for (int i = 1; i < n + 1; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < m; i++) {
            StringTokenizer st2 = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(st2.nextToken());
            int b = Integer.parseInt(st2.nextToken());

            graph[a].add(b);
            graph[b].add(a);
        }

        // 오름차순 방문을 위한 정렬
        for (int i = 1; i < n + 1; i++) {
            Collections.sort(graph[i]);
        }

        boolean[] dfsVisited = new boolean[n + 1];
        sb.append(depthFirstSearch(graph, dfsVisited, k)).append("\n");

        boolean[] bfsVisited = new boolean[n + 1];
        sb.append(breadthFirstSearch(graph, bfsVisited, k));

        System.out.println(sb);
    }

    /**
     * DFS - 재귀함수를 사용한다.
     * @param graph
     * @param visited
     * @param index
     * @return
     */
    private static String depthFirstSearch(List<Integer>[] graph, boolean[] visited, int index) {
        StringBuilder sb = new StringBuilder();

        visited[index] = true;
        sb.append(index).append(" ");

        for (int next : graph[index]) {
            if (!visited[next]) {
                 sb.append(depthFirstSearch(graph, visited, next));
            }
        }

        return sb.toString();
    }

    /**
     * BFS - Queue를 사용한다.
     * @param graph
     * @param visited
     * @param index
     * @return
     */
    private static String breadthFirstSearch(List<Integer>[] graph, boolean[] visited, int index) {
        StringBuilder sb = new StringBuilder();
        Queue<Integer> queue = new LinkedList<>();

        queue.offer(index);
        visited[index] = true;

        while (!queue.isEmpty()) {
            int current = queue.poll();
            sb.append(current).append(" ");

            for (int next : graph[current]) {
                if (!visited[next]) {
                    visited[next] = true;
                    queue.offer(next);
                }
            }
        }

        return sb.toString();
    }
}
