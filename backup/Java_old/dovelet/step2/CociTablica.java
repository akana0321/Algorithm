package dovelet.step2;

import java.io.*;
import java.util.*;

public class CociTablica {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		List<Integer> table = new ArrayList<>();
		Map<Integer, Float> compute = new HashMap<>();
		
		for(int i=0; i<2; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			while(st.hasMoreTokens()) {
				table.add(Integer.parseInt(st.nextToken()));
			}
		}
		
		compute.put(0, (float)table.get(0)/table.get(2) + (float)table.get(1)/table.get(3));
		compute.put(1, (float)table.get(0)/table.get(1) + (float)table.get(2)/table.get(3));
		compute.put(2, (float)table.get(2)/table.get(0) +  (float)table.get(3)/table.get(1));
		compute.put(3, (float)table.get(1)/table.get(0) + (float)table.get(3)/table.get(2));
		
		List<Integer> keySet = new ArrayList<>(compute.keySet());
		keySet.sort((o1, o2) -> compute.get(o2).compareTo(compute.get(o1)));
		
		System.out.println(keySet.get(0));
	}
}
