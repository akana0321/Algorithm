package dovelet.step3;

import java.io.*;
import java.util.*;

public class ModularInverse {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		int x = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		for(int i=1; i<m; i++) {
			if((x*i)%m == 1) {
				System.out.println(i);
				System.exit(0);
			}
		}
		System.out.println("No such integer exists.");
	}
}
