package dovelet.step2;

import java.io.*;
import java.util.*;

public class Queen {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		long n = Long.parseLong(st.nextToken());
		long m = Long.parseLong(st.nextToken());
		long result = n > m ? m : n;
		System.out.println(result);
	}
}
