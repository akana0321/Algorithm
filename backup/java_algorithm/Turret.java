package java_algorithm;

import java.util.*;

/*
 * 터렛(https://www.acmicpc.net/problem/1002)
 */

public class Turret {
	public static int searchPoint(int x1, int y1, int r1, int x2, int y2, int r2) {
		int distancePow = (int)(Math.pow(x1 - x2, 2) + Math.pow(y1 - y2, 2));
		
		if(x1 == x2 && y1 == y2 && r1 == r2) 		// 중점이 같으면서 반지름도 같을 경우(동일한 원)
			return -1;
		else if(distancePow > Math.pow(r1 + r2, 2))	// 두 원의 반지름 합보다 중점간 거리가 더 길 때(외접 X) 
			return 0;
		else if(distancePow < Math.pow(r1 - r2, 2))	// 원 안에 원이 있으나 내접하지 않을 때(내접 X)
			return 0;
		else if(distancePow == Math.pow(r2 - r1, 2))	// 내접할 때
			return 1;
		else if(distancePow == Math.pow(r1 + r2, 2))	// 외접할 때
			return 1;
		else										// 위의 경우를 제외하면 두 점에서 만나는 경우 밖에 없음
			return 2;
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int tc = Integer.parseInt(sc.nextLine());
		String[] temp;
		for(int i=0; i<tc; i++) {
			temp = sc.nextLine().split(" ");
			System.out.println(searchPoint(Integer.parseInt(temp[0]), Integer.parseInt(temp[1]), Integer.parseInt(temp[2]),
					Integer.parseInt(temp[3]), Integer.parseInt(temp[4]), Integer.parseInt(temp[5])));
		}
	}
}
