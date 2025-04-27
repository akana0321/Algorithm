package java_algorithm;

import java.util.Scanner;

public class Word4 {

	public static void main(String[] args) {
	      Scanner scan = new Scanner(System.in);
	       String[] input = (scan.nextLine()).split(" ");
	       
	      int n = Integer.parseInt(input[0]);//지혜가 암기할 수 있는 단어 갯수
	      int w = Integer.parseInt(input[1]);//주어진 단어 갯수
	      int sec = 0;// 총 걸린 시간
	      int p = 0;
	      String[] word = (scan.nextLine()).split(" "); //단어
	      String[] head = new String[n];//지혜가 암기하는 단어를 저장할 배열
	      boolean exist = false;
	      
	      //단어들 비교
	       //head[0]이 제일 오래된 것
	      for(int i=0; i<w; i++) {
	         //지혜 머리에 단어가 존재하는지
	         exist = false;
	         for(int j=0; j<n; j++) {
	            if(head[j] == null) continue;
	            if(head[j].equals(word[i])) {
	               exist = true;
	               p = j;
	               break;
	            }
	         }
	         //머리에 있는 경우
	         if(exist) {
	            sec += 1;
	            
	            for(int j = p; j<n-1; j++) {
	               if(head[j+1] == null) {
	                  head[j] = word[i];
	                  break;
	               }
	               head[j] = head[j+1];
	               if(j == n-2) {
	                  head[n-1] = word[i];
	               }
	            }
	         }else if(!exist && head[n-1] != null) { //머리에 없지만 꽉찬 경우
	            sec += 3;
	            int sum = 0;
	            int avg = 0;
	            for(int j=0; j<w; j++) {
	               sum += word[j].length();
	            }
	            avg = sum / w;
	            
	            for(int j=0; j<n-1; j++) {
	               if(head[j].length() <= avg) {
	                  for(int k=j; k<n-1; k++) {
	                     head[k] = head[k+1];
	                  }
	                  head[n-1] = word[i];
	                  break;
	               }
	            }
	         }else { //머리에 없지만 꽉차지 않은 경우
	            for(int m = 0; m<n; m++) {
	               if(head[m] == null) {
	                  head[m] = word[i];
	                  sec += 3;
	                  break;
	               }
	            }
	         }
	      }
	      System.out.println("걸린 시간을 초 단위로 출력\n");
	      System.out.println(sec);


	}

}
