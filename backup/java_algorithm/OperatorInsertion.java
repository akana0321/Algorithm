package java_algorithm;

import java.util.*;

public class OperatorInsertion {
	// 정적 필드로 선언(메소드 내 어디서나 접근할 수 있도록 하기 위해)
	static int max = Integer.MIN_VALUE;		// 최대값(초기는 int의 최저값으로 선언:비교하면서 갱신하기 때문)
	static int min = Integer.MAX_VALUE;		// 최소값(초기는 int의 최대값으로 선언)
	static int n;							// 주어지는 숫자의 개수
	static int[] nums;						// 주어지는 숫자들의 배열
	static int[] operators = new int[4];	// 0:+, 1:-, 2:x, 3:/
	/*
	 * 시작 숫자에서 마지막 숫자까지 현재 가능한 연산으로 마지막 숫자까지 갔다가
	 * 마지막 단계에서 나온 값을 최대값과 최솟값과 비교하여 갱신할 수 있다면 갱신하고 함수 종료
	 * 
	 * 여기서 operation 메소드는 시작 숫자부터 마지막 숫자까지 가는 것
	 * operation 메소드 안의 for문과 switch문은 각 연산의 경우
	 */	
	public static void operation(int num, int count) {	// num은 해당 시점의 수, count는 반복 회수
		if(count == n) {					// n번만큼 반복을 했다면 모든 숫자를 다 돌았다는 것
			max = (num > max) ? num : max;	// 연산의 마지막 값인 num과 max값을 비교
			min = (num < min) ? num : min;	// 연산의 마지막 값인 num과 min값을 비교
			return;							// 해당 메소드 종료
		}
		
		for(int i=0; i<4; i++) {
			if(operators[i] > 0) {	// 연산의 개수가 한 개 이상이어야 연산이 가능하므로
				operators[i] -= 1;	// 해당 연산 시작
				
				switch(i) {	// operator[i]는 각 연산의 횟수를 의미하므로 i는 해당 연산을 의미
					case 0:	// 더하기
						operation(num + nums[count], count+1);
						break;
					case 1:	// 빼기
						operation(num - nums[count], count+1);
						break;
					case 2:	// 곱하기
						operation(num * nums[count], count+1);
						break;
					case 3: // 나누기
						operation(num / nums[count], count+1);
						break;
				}
				operators[i] += 1;	// 해당 연산이 끝났으므로 다시 다른 경우를 탐색하기 위해 복구
			}
		}
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = Integer.parseInt(sc.nextLine());	// 숫자의 개수
		nums = new int[n];							// 주어지는 숫자의 개수만큼 배열 선언
		String[] temp = sc.nextLine().split(" ");	// 입력을 임시로 저장
		for(int i=0; i<n; i++) {
			nums[i] = Integer.parseInt(temp[i]);	// int 타입으로 변경
		}
		temp = sc.nextLine().split(" ");			// 연산자들의 각 개수를 받음
		sc.close();									// Scanner 쓸 일 없으니 닫음
		for(int i=0; i<4; i++) {
			operators[i] = Integer.parseInt(temp[i]);	// int 타입으로 변경
		}
		
		operation(nums[0], 1);
		System.out.println(max);
		System.out.println(min);
	}
}
