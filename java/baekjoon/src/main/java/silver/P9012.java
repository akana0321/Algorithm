package silver;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;

/**
 * 9012 괄호
 * https://www.acmicpc.net/problem/9012
 */
public class P9012 {
    private static char PARENTHESIS_OPEN = '(';
    private static char PARENTHESIS_CLOSE = ')';

    public static void run() throws Exception {
        StringBuilder result = new StringBuilder();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            String target = br.readLine();

            result.append(checkVps(target)).append('\n');
        }

        System.out.println(result);
    }

    /**
     * VPS 여부를 체크한다
     * @param target 대상문자
     * @return "NO" | "YES"
     */
    private static String checkVps(String target) {
        String result = "NO";

        // 일단 길이가 홀수면 쌍이 아니기 때문에 VPS가 아님
        if (target.length() % 2 == 1) {
            return result;
        }

        Stack<Character> parenthesesOpenStack = new Stack<>();

        for (int i = 0; i < target.length(); i++) {
            if (target.charAt(i) == PARENTHESIS_OPEN) {
                parenthesesOpenStack.push(target.charAt(i));
            } else {
                if (parenthesesOpenStack.isEmpty()) {
                    return result;
                } else {
                    parenthesesOpenStack.pop();
                }
            }
        }

        if (parenthesesOpenStack.isEmpty()) {
            result = "YES";
        }

        return result;
    }
}
