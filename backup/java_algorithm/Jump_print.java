package java_algorithm;

import java.util.*;

public class Jump_print {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int size = Integer.parseInt(sc.nextLine());	// 판의 사이즈
		int[][] board = new int[size][size];		// 보드의 크기
		for(int i=0; i<size; i++) {
			String[] info = sc.nextLine().split(" ");			// 한 줄의 정보
			for(int j=0; j<size; j++) {
				board[i][j] = Integer.parseInt(info[j]);		// 보드 정보 삽입
			}
		}
		sc.close();
		
		long[][] situation = new long[size][size];				// 해당 위치에 가는 경우의 수
		situation[0][0] = 1;									// 처음은 한가지
		System.out.println(situation[size-1][size-1]);
		for(int i=0; i<size; i++) {
			for(int j=0; j<size; j++) {
				System.out.print(situation[i][j] + " ");
			}
			System.out.println();
		}
		
		for(int i=0; i<size; i++) {
			for(int j=0; j<size; j++) {
				if(i == size-1 && j == size-1) {				// 
					break;
				}
				int nextX = i + board[i][j];
				int nextY = j + board[i][j];
				System.out.println("i, j: " + i + ", " + j);
				System.out.println("nextX, nextY: " + nextX + ", " + nextY);
				if(nextX < size) {
					situation[nextX][j] += situation[i][j];
				}
				if(nextY < size) {
					situation[i][nextY] += situation[i][j];
				}
				
				for(int k=0; k<size; k++) {
					for(int l=0; l<size; l++) {
						System.out.print(situation[k][l] + " ");
					}
					System.out.println();
				}
				System.out.println();
			}
		}
		
//		System.out.println(situation[size-1][size-1]);
		for(int i=0; i<size; i++) {
			for(int j=0; j<size; j++) {
				System.out.print(situation[i][j] + " ");
			}
			System.out.println();
		}
	}
}
