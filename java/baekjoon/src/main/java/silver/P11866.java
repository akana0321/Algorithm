package silver;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

/**
 * 11866 요세푸스 문제0
 * https://www.acmicpc.net/problem/11866
 */
public class P11866 {
    public static void run() throws Exception {
        StringBuilder result = new StringBuilder();
        result.append("<");

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k =  Integer.parseInt(st.nextToken());

        Queue<Integer> queue = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            queue.offer(i + 1);
        }

        int counter = 1;
        while (queue.size() > 1) {
            if (counter < k) {
                queue.offer(queue.poll());
                counter++;
            } else {
                result.append(queue.poll()).append(", ");
                counter = 1;
            }
        }

        result.append(queue.poll()).append(">");
        System.out.println(result);
    }
}
