package java_algorithm;

import java.util.*;

public class Repairman {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String[] nl = sc.nextLine().split(" ");
		int n = Integer.parseInt(nl[0]);		// 물이 새는 곳의 개수
		int l = Integer.parseInt(nl[1]);		// 테이프의 길이
		String[] strLeak = sc.nextLine().split(" ");	// 물이 새는 곳의 위치(String)
		int[] leak = new int[n];				// 물의 새는 곳의 위치(int)
		int result = 0;							// 결과(필요한 테이프의 개수)
		sc.close();
		
		// 정수 형태로 변환
		for(int i=0; i<n; i++) {
			leak[i] = Integer.parseInt(strLeak[i]);
		}
		
//		Arrays.sort(leak); 라이브러리 사용
		
		// 위치가 순서대로 주어지지 않으므로 정렬 수행
		for(int i=0; i<n-1; i++) {
			for(int j=i+1; j<n; j++) {
				if(leak[i] > leak[j]) {
					int temp = leak[i];
					leak[i] = leak[j];
					leak[j] = temp;
				}
			}
		}
		
		double end = 0; // 테이프가 끝나는 부분
		for(int i=0; i<n; i++) {
			if(leak[i] + 0.5 > end) { 		// 현재 테이프의 끝점보다 멀리 있는 경우
				result += 1;				// 테이프 개수 추가
				end = leak[i] - 0.5 + l;	// 테이프 마지막 지점 갱신
			}
		}
		
		System.out.println(result);
	}
}
