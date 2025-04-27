package dovelet.step2;

import java.io.*;
import java.util.*;

public class Can {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		int black = Integer.parseInt(st.nextToken());
		int white = Integer.parseInt(st.nextToken());
		
		if(white%2 == 0) {
			System.out.println("black");
		} else {
			System.out.println("white");
		}
	}
}
