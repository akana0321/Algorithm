package dovelet.step3;

import java.io.*;
import java.util.*;

public class Parking {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		List<Integer> list = new ArrayList<>();
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		for(int i=0; i<n; i++)
			list.add(Integer.parseInt(st.nextToken()));
		Collections.sort(list);
		
		System.out.println((list.get(list.size()-1) - list.get(0))*2);
	}
}
