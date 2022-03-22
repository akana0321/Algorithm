package java_algorithm;

import java.util.Scanner;

public class StepMount2 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String road = sc.nextLine();	// 주어지는 길
		boolean sharp = false;			// 급경사 판단
		char[] roadStack = new char[road.length()];	// 
		int height = 0;					// 계단의 높이
		int result = 0;					// 열량
		
		for(int i=0; i<road.length(); i++) {	// 등산로를 하나씩 확인
			System.out.println(i + "번째 result: " + result);
			if(road.charAt(i) == '(') {			// 올라가는 길
				if(sharp) {						// 급경사 상태라면
					height++;					// 우선 높이를 1증가시키고
					result += (height * 2);		// 두 배를 함
				} else {						// 급경사가 아니라면
					height++;					// 높이를 1 증가시키고
					result += height;			// 더함
				}
			} else if(road.charAt(i) == ')') {	// 내려오는 길
				if(sharp) {						// 급경사라면
					result += (height * 2);		// 우선 2배를 해서 더해주고
					height--;					// 높이를 1 감소
				} else {						// 급경사가 아니라면
					result += height;			// 높이를 더해주고
					height--;					// 높이 1 감소
				}
			} else {							// 급경사
				if(sharp == false) {			// 급경사가 아닌 상태라면
					sharp = true;				// 급경사 시작
				} else {						// 급경사 상태였다면
					sharp = false;				// 급경사가 끝남
				}
			}
		}
		
		System.out.println("길용이가 소모하는 칼로리를 단위를 생략한 채 정수만 출력\n");
		System.out.println(result);
	}
}
