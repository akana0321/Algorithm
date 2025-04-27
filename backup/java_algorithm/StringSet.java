package java_algorithm;

import java.util.*;

public class StringSet {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String[] nm = sc.nextLine().split(" ");
		int n = Integer.parseInt(nm[0]);		// 주어진 문자열의 개수
		int m = Integer.parseInt(nm[1]);		// 검사해야하는 문자열의 개수
		String[] target = new String[n];		// 주어진 문자열
		int result = 0;							// 결과
		
		// 주어진 문자열 저장
		for(int i=0; i<n; i++) {
			target[i] = sc.nextLine();
		}
		
		// s를 입력 받으며 target의 문자열 중 포함되는 것이 있는지 확인
		for(int i=0; i<m; i++) {
			String s = sc.nextLine();
			for(int j=0; j<n; j++) {
				if(target[j].equals(s)) {
					result += 1;
					break;
				}
			}
		}
		sc.close();
		System.out.println(result);
	}
}
