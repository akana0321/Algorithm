package java_algorithm;

import java.util.*;

public class Repairman2 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
	      
	      String first = sc.nextLine();
	      int N = Integer.parseInt(first.split(" ")[0]);
	      int L = Integer.parseInt(first.split(" ")[1]);
	      
	      String second = sc.nextLine();
	      String[] location = second.split(" ");
	      int[] intLocation = new int[N];
	      
	      for(int i=0; i<N; i++) {
	    	  intLocation[i] = Integer.parseInt(location[i]);
	      }
	      
	      // 위치가 순서대로 주어지지 않으므로 정렬 수행
			for(int i=0; i<N-1; i++) {
				for(int j=i+1; j<N; j++) {
					if(intLocation[i] > intLocation[j]) {
						int temp = intLocation[i];
						intLocation[i] = intLocation[j];
						intLocation[j] = temp;
					}
				}
			}
			
	      
	      //시작하자마자 테이프 붙이고 시작
	      int count = 1;
	      
	      int index = 0;	      
	      for(int i = index + 1; i < N; i++) {
	    	  System.out.println("************ "+(i+1) + "번째 ******************");
	    	  System.out.println(intLocation[index] + " " + intLocation[i]);
	    	  System.out.println(index);
	    	  System.out.println("************************************\n");
	    	  if(intLocation[index] + L - 1 < intLocation[i]) {
	            count++;
	            index = i;
	         }
	      }
	      
	      System.out.println(count);
	   }

}
