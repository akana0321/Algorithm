package baekjoon;

import java.io.*;
import java.util.*;

public class LostBracket {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), "-");
		List<String> list = new ArrayList<>();
		int result = 0;
		
		while(st.hasMoreTokens()) {
			list.add(st.nextToken());
		}
		
		st = new StringTokenizer(list.get(0), "+");
		while(st.hasMoreTokens())
			result += Integer.parseInt(st.nextToken());
		
		for(int i=1; i<list.size(); i++) {
			st = new StringTokenizer(list.get(i), "+");
			int temp = 0;
			while(st.hasMoreTokens()) {
				temp += Integer.parseInt(st.nextToken());
			}
			result -= temp;
		}
		
		System.out.println(result);
	}
}
