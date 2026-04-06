package silver;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;

/**
 * 1874 스택수열
 * https://www.acmicpc.net/problem/1874
 */
public class P1874 {
    public static void run() throws Exception {
        StringBuilder result = new StringBuilder();

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        Stack<Integer> stack = new Stack<>();
        int stackNum = 1;

        for (int i = 0; i < n; i++) {
            int inputNum = Integer.parseInt(br.readLine());

            // 스택숫자가 입력받은 숫자보다 작다면 같아질 때까지 push
            while (stackNum <= inputNum) {
                stack.push(stackNum++);
                result.append("+").append("\n");
            }

            // 스택이 비어있지 않고 상단의 수와 입력받은 숫자와 같다면 pop
            if (!stack.isEmpty() && stack.peek() == inputNum) {
                stack.pop();
                result.append("-").append("\n");
            } else {
                // 스택이 비어있거나 상단의 수와 다를 경우 NO
                System.out.println("NO");
                return;
            }
        }

        if (!stack.isEmpty()) {
            System.out.println("NO");
            return;
        }

        System.out.println(result);
    }
}
