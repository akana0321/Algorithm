package silver;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

/**
 * 2178 미로탐색
 * https://www.acmicpc.net/problem/2178
 */
public class P2178 {
    public static void run() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[][] maze = new int[n][m];
        for (int i = 0; i < n; i++) {
            String row =  br.readLine();

            for (int j = 0; j < m; j++) {
                maze[i][j] = row.charAt(j) - '0';
            }
        }

        boolean[][] visited = new boolean[n][m];

        breadthFirstSearch(maze, visited, 0, 0, n, m);

        System.out.println(maze[n - 1][m - 1]);
    }

    private static void breadthFirstSearch(int[][] maze, boolean[][] visited, int startX, int startY, int endX, int endY) {
        // 상하좌우 움직일 수 있는 위치
        int[] dx = { -1, 1, 0, 0 };
        int[] dy = { 0, 0, -1, 1 };

        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{startX, startY});
        visited[startX][startY] = true;

        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int cx = current[0];
            int cy = current[1];

            for (int i = 0; i < 4; i++) {
                int nx = cx + dx[i];
                int ny = cy + dy[i];

                // 범위 밖
                if (nx < 0 || ny < 0 || nx >= endX || ny >= endY) {
                    continue;
                }

                // 벽이거나 이미 방문
                if (maze[nx][ny] == 0 || visited[nx][ny]) {
                    continue;
                }

                visited[nx][ny] = true;
                maze[nx][ny] = maze[cx][cy] + 1;
                queue.offer(new int[]{nx, ny});
            }
        }
    }
}
