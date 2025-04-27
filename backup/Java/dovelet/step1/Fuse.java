package dovelet.step1;

import java.io.*;
import java.util.*;

public class Fuse {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		float computer = Float.parseFloat(st.nextToken()) * 2.5f;
		float printer = Float.parseFloat(st.nextToken()) * 2;
		float router = Float.parseFloat(st.nextToken()) * 0.5f;
		
		float total = computer + printer + router;
		int answer = (int)Math.ceil((total * 2) / 10) * 10;
		System.out.println(answer + " amperes");
	}
}
