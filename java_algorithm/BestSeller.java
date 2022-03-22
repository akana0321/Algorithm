package java_algorithm;

import java.util.*;
import java.lang.*;
import java.io.*;

public class BestSeller {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		ArrayList<String> list = new ArrayList<>();
		int n = Integer.parseInt(br.readLine());
		HashMap<String, Integer> map = new HashMap<>();
		for(int i=0; i<n; i++) {
			String book = br.readLine();
			if(map.containsKey(book))
				map.replace(book, map.get(book) + 1);
			else
				map.put(book, 0);
		}
		
		int max = -1;
		for(String s : map.keySet()) {
			max = Math.max(max, map.get(s));
		}
		
		list = new ArrayList<String>(map.keySet());
		Collections.sort(list);
		for(String s : list) {
			if(map.get(s) == max) {
				System.out.println(s);
				break;
			}
		}
	}
}
