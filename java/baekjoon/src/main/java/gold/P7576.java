package gold;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

/**
 * 7576 토마토
 * https://www.acmicpc.net/problem/7576
 */
public class P7576 {
    // 상하좌우 pair
    private static int[] dx = new int[] {-1, 1, 0, 0};
    private static int[] dy = new int[] {0, 0, -1, 1};

    public static void run() throws Exception {
        int result = 0;

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int m =  Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());

        int[][] box = new int[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                box[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        breadthFirstSearch(box, n, m);

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (box[i][j] == 0) {
                    System.out.println("-1");
                    return;
                }

                result = result > box[i][j] ? result : box[i][j];
            }
        }

        System.out.println(result - 1);
    }

    private static int breadthFirstSearch(int[][] box, int endX, int endY) {
        int result = 0;

        // 익은 토마토만 들어가는 queue
        Queue<int[]> queue = new LinkedList<>();

        // 익은 토마토(1)가 있는 위치 정보를 queue에 담는다
        for (int i = 0; i < endX; i++) {
            for (int j = 0; j < endY; j++) {
                if (box[i][j] == 1) {
                    queue.offer(new int[]{i, j});
                }
            }
        }

        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int currentX = cur[0];
            int currentY = cur[1];

            for (int i = 0; i < 4; i++) {
                int newX = cur[0] + dx[i];
                int newY = cur[1] + dy[i];

                // 범위를 벗어나면 continue
                if (newX >= endX || newY >= endY || newX < 0 || newY < 0) {
                    continue;
                }

                // 토마토가 없거나 이미 익은 토마토면 continue
                if (box[newX][newY] == -1 || box[newX][newY] > 0) {
                    continue;
                }

                box[newX][newY] = box[currentX][currentY] + 1;

                queue.offer(new int[]{newX, newY});
            }

            /* 단계별 결과 확인 로그
            for (int i = 0; i < endX; i++) {
                for (int j = 0; j < endY; j++) {
                    System.out.print(box[i][j] + " ");
                }
                System.out.println();
            }
            System.out.println();
            */
        }

        return result;
    }
}
