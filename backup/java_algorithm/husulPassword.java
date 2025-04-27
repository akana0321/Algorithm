package java_algorithm;

import java.util.*;

/* 주어진 입력
2
9
ohkllufku
7
hkraukq
 */

public class husulPassword {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = Integer.parseInt(sc.nextLine());	// 테스트 케이스의 개수
		int check = 0;								// 'w'와 같거나 더 뒤의 알파벳인지 체크
		
		// 테스트 케이스 회수만큼 반복
		for(int i=0; i<t; i++) {
			int length = Integer.parseInt(sc.nextLine());	// 암호의 길이
			String password = sc.nextLine();				// 암호 해독 전
			String result = "";								// 결과
			for(int j=0; j<length; j++) {					// 암호문의 알파벳을 하나씩 돌면서
				check = password.charAt(j) - 'w';			// 해당 값이 0 이상이면 'w'와 같거나 더 뒤의 단어인 것
				if(check >= 0) {							// 만약 'w'랑 같거나 더 뒤의 알파벳이면
					result += (char)('a' + check);			// 'w'의 4칸 뒤는 a니까 check만큼 더해줘서 나온 알파벳을 결과에 이음
				} else {									// 'w'보다 길지 않다면
					result += (char)(password.charAt(j) + 4);	// 4칸만 이동하여 나온 알파벳을 결과에 이어줌
				}
			}
			System.out.println("Case#" + (i+1));
			System.out.println(result);
		}
	}
}
