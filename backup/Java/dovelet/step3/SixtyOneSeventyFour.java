package dovelet.step3;
// 6174
// 왠지는 모르겠는데 runtime 오류 뜸
import java.io.*;
import java.util.*;

public class SixtyOneSeventyFour {
	public static int linkNumbers(PriorityQueue<Integer> pq) {
		StringBuilder sb = new StringBuilder();
		
		while(!pq.isEmpty()) {
			sb.append(pq.poll());
		}
		
		return Integer.parseInt(sb.toString());
	}
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		PriorityQueue<Integer> minNum = new PriorityQueue<>();
		PriorityQueue<Integer> maxNum = new PriorityQueue<>(Collections.reverseOrder());
		int result = 0;
		
		String target = br.readLine();
		
		while(!target.equals("6174")) {			
			for(int i=0; i<target.length(); i++) {
				int ele = Character.getNumericValue(target.charAt(i));
				maxNum.offer(ele);
				minNum.offer(ele);
			}
			
			target = String.valueOf(linkNumbers(maxNum)  - linkNumbers(minNum));
			result++;
		}
		System.out.println(result);
	}
}
