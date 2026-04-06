package silver;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;

/**
 * 2164 카드2
 * https://www.acmicpc.net/problem/2164
 */
public class P2164 {
    public static void run() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        Queue<Integer> queue = new ArrayDeque<>();
        for (int i = 1; i <= n; i++) {
            queue.offer(i);
        }

        while (queue.size() > 1) {
            queue.poll();
            queue.offer(queue.poll());
        }

        System.out.println(queue.peek());
    }
}
