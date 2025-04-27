package dovelet.step3;

import java.io.*;
import java.util.*;

public class TriangularSum {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int wN = 0;
		int tN = 1;
		
		for(int i=1; i<=n; i++) {
			tN += (i+1);
			wN += i * tN;
		}
		
		System.out.println(wN);
	}
}
