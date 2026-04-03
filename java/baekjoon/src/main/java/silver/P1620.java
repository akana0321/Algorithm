package silver;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

/**
 * 1620 나는 포켓몬 마스터 이다솜
 * https://www.acmicpc.net/problem/1620
 */
public class P1620 {
    public static void run() throws Exception {
        StringBuilder result = new StringBuilder();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        // 수록 되어 있는 수
        int n = Integer.parseInt(st.nextToken());
        // 맞춰야 하는 문제 수
        int m = Integer.parseInt(st.nextToken());

        Map<String, Integer> nameWithSeqMap = new HashMap<>();
        List<String> nameList = new ArrayList<>();

        // 숫자가 들어오면 숫자에 해당하는 이름을, 이름이 들어오면 이름에 해당하는 순번을
        for (int i = 0; i < n; i++) {
            String name = br.readLine();
            nameWithSeqMap.put(name, i);
            nameList.add(name);
        }

        for (int i = 0; i < m; i++) {
            String question = br.readLine();

            try {
                // 파싱해서 숫자면 이름 출력
                int seq = Integer.parseInt(question);
                result.append(nameList.get(seq - 1)).append("\n");
            } catch (NumberFormatException e) {
                // 파싱 실패 시 숫자가 아니므로 이름에 해당하는 순번 출력
                int seq = nameWithSeqMap.get(question);
                result.append(seq + 1).append("\n");
            }
        }

        System.out.println(result);
    }
}
