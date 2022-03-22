package java_algorithm;

import java.util.*;

public class Jump {
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
		situation[0][0] = 1;									// 시작은 무조건 하는 것, 0으로 설정할 시 이후 이동 모두 0이 됨
		
		for(int i=0; i<size; i++) {
			for(int j=0; j<size; j++) {
				if(i == size-1 && j == size-1) {				// (i, j)가 목적지인 경우
					break;
				}
				int nextX = i + board[i][j];					// 오른쪽으로 가는 경우
				int nextY = j + board[i][j];					// 아래로 가는 경우
				if(nextX < size) {
					situation[nextX][j] += situation[i][j];		// (i, j)에서 (nextX, j)로 가는 경우
				}
				if(nextY < size) {
					situation[i][nextY] += situation[i][j];		// (i, j)에서 (i, nextY)로가는 경우
				}
			}
		}		
		System.out.println(situation[size-1][size-1]);			// 목적지의 경우의 수 출력
	}
}
