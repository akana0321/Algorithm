package java_algorithm;

import java.util.Scanner;

public class question03 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int result = 0;
		int n = Integer.parseInt(sc.nextLine());
		String[] scores = new String[n];
		String[] obstacles = new String[2];
		scores = sc.nextLine().split(" ");
		for(int i=0; i<obstacles.length; i++) {
			obstacles[i] = sc.nextLine();
		}
		
		for(int i=0; i<n; i++) {
			if(obstacles[0].charAt(i) == 'X' || obstacles[1].charAt(i) == 'X') {
				continue;
			} else {
				result += Integer.parseInt(scores[i]);
			}
		}
		
		System.out.println("총 점수\n");
		System.out.println(result);
	}
}
