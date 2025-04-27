package dovelet.step2;

import java.io.*;
import java.util.*;

public class CociKornislav {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		List<Integer> lines = new ArrayList<>();
		
		for(int i=0; i<4; i++)
			lines.add(Integer.parseInt(st.nextToken()));
		
		Collections.sort(lines);
		
		System.out.println(Math.min(lines.get(0), lines.get(1)) * Math.min(lines.get(2), lines.get(3)));
	}
}
