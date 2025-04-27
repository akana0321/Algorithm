package baekjoon;

import java.io.*;
import java.util.*;

public class BlackJack {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		List<Integer> cards = new ArrayList<>();
		int answer = 0;
		
		String[] condition = br.readLine().split(" ");
		int count = Integer.parseInt(condition[0]);
		int target = Integer.parseInt(condition[1]);
		String[] strDraws = br.readLine().split(" ");
		for(String strDraw : strDraws)
			cards.add(Integer.parseInt(strDraw));
		Collections.sort(cards);
		
		for(int i=cards.size()-1; i>=0; i--) {
			if(cards.get(i) >= target) {
				cards.remove(i);
			} else {
				break;
			}
		}
		
		for(int i=0; i<cards.size()-2; i++) {
			for(int j=i+1; j<cards.size(); j++) {
				for(int k=j+1; k<cards.size(); k++) {
					int temp = cards.get(i) + cards.get(j) + cards.get(k);
					if(temp == target) {
						System.out.println(temp);
						System.exit(0);
					}
					if(temp < target && temp > answer)
						answer = temp;
				}
			}
		}
		
		System.out.println(answer);
	}
}
