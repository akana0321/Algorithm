package java_algorithm;

import java.util.Scanner;

public class WordMemorization {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String[] nw = sc.nextLine().split(" ");
		int n = Integer.parseInt(nw[0]);	// 기억할 수 있는 단어의 수
		int w = Integer.parseInt(nw[1]);	// 주어지는 단어의 수
		
		String[] memo = new String[n];		// 단어를 기억하는 공간
		String[] words = new String[w];		//  주어지는단어 목록
		words = sc.nextLine().split(" ");	// 공백 기준으로 분리하여 배열로 만듬
		int result = 0;						// 걸리는 시간
		boolean checkWord = false;			// memo 배열에서 words[i]가 있는지 판단하는 논리 타입 변수
		int memoLength = 0;					// memo 배열에서 단어의 총 길이
		boolean checkMemo = false;			// memo 배열에서 단어를 삭제해야 하는지 판단하는 논리 타입 변수
		
		
	}                                
}
