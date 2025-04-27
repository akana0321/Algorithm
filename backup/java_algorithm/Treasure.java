package java_algorithm;

import java.util.*;

/*
 * 보물(https://www.acmicpc.net/problem/1026)
 */
public class Treasure {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = Integer.parseInt(sc.nextLine());	// 수열의 크기
		int[] a = new int[n];						// 배열 A
		int[] b = new int[n];						// 배열 B
		String[] temp = sc.nextLine().split(" ");
		for(int i=0; i<n; i++)
			a[i] = Integer.parseInt(temp[i]);
		temp = sc.nextLine().split(" ");
		for(int i=0; i<n; i++)
			b[i] = Integer.parseInt(temp[i]);
		int result = 0;
		sc.close();
		
		Arrays.sort(a);	// a 정렬
		Arrays.sort(b);	// b 정렬
		
		for(int i=0; i<n; i++) {
			result += (a[i] * b[n-1-i]);	// a의 가장 작은값, b의 가장 큰 값을 곱해 더함
		}
		
		System.out.println(result);
	}
}
