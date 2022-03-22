package java_algorithm;

import java.util.Scanner;

public class OddNum {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String[] nums = sc.nextLine().split(", ");	// 숫자 배열
		int num = 0;	// 숫자 하나
		int oddSum = 0;	// 홀수의 합
		int oddMin = 0;	// 홀수 중 최소값
		
		for(int i=0; i<7; i++) {
			num = Integer.parseInt(nums[i]);
			if(num%2 == 1) {		// 만약 홀수라면
				oddSum += num;		// 홀수의 합에 더함
				
				if(oddMin == 0) {	// 만약 홀수 중 최소값이 초기상태라면
					oddMin = num;	// num을 대입
				} else {
					if(num < oddMin) {	// num이 더 작다면
						oddMin = num;	// oddMin 갱신
					}
				}
			}
		}
		
		if(oddSum == 0) {
			System.out.println(-1);
		} else {
			System.out.println(oddSum);
			System.out.println(oddMin);
		}
	}
}
