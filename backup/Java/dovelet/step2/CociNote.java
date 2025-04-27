package dovelet.step2;

import java.io.*;
import java.util.*;

public class CociNote {
	public static String getResult(int result) {
		if(result == 1) {
			return "ascending";
		} else if(result == -1) {
			return "descending";
		} else {
			return "mixed";
		}
	}
	
	public static int checkOrder(List<Integer> list, int index) {
		if(list.get(index) < list.get(index+1)) {
			return 1;
		} else {
			return -1;
		}
	}
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		int result = 0;
		
		List<Integer> notes = new ArrayList<>();
		
		for(int i=0; i<8; i++)
			notes.add(Integer.parseInt(st.nextToken()));
		
		result = checkOrder(notes, 0);
		
		for(int i=1; i<7; i++) {
			int temp = checkOrder(notes, i);
			if(temp != result) {
				result = 0;
				break;
			}
		}
		
		System.out.println(getResult(result));
	}
}
