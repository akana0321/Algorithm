package dovelet.step2;

import java.io.*;
import java.util.*;

public class Cross {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int[] line1 = new int[2];
		int[] line2 = new int[2];
		
		String[] input = br.readLine().split(" ");
		line1[0] = Integer.parseInt(input[0]);
		line1[1] = Integer.parseInt(input[1]);
		input = br.readLine().split(" ");
		line2[0] = Integer.parseInt(input[0]);
		line2[1] = Integer.parseInt(input[1]);
		
		Arrays.sort(line1);
		Arrays.sort(line2);
		
		if((line1[0] < line2[0] && line1[1] > line2[1]) || (line1[0] > line2[1] && line1[1] > line2[0])
			|| (line1[0] > line2[0] && line1[1] < line2[1]) || (line1[0] < line2[1] && line1[1] < line2[0])) {
			System.out.println("not cross");
		} else {
			System.out.println("cross");
		}
	}
}
