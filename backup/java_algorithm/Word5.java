package java_algorithm;

import java.util.ArrayList;
import java.util.Scanner;


public class Word5 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int res=0; //결과값
		ArrayList <String> word = new ArrayList<String>();  //단어 리스트
	    ArrayList <String> mind = new ArrayList<String>();  // 암기 리스트
		Scanner scanner = new Scanner(System.in);
		String start=scanner.nextLine();
		String[] str=start.split(" ");
		int n=Integer.parseInt(str[0]);  //스플릿으로 n,w 삽입
		int w=Integer.parseInt(str[1]);
	    String s=scanner.nextLine();
	    String[] s2=s.split(" ");
	    for(int i=0;i<s2.length;i++) {  //스플릿으로 단어 삽입
	    	word.add(s2[i]);
	    }
	    
	   mind.add(word.get(0));  //첫번째 단어 삽입
	    res+=3;    //시간 3초 증가
	    for(int i=1;i<word.size();i++) {
	    	boolean chk1=false;   // 암기 갯수보다 적은경우 continue
	    	boolean chk2=false;   //암기 갯수보다 많은경우 continue
	    	if(mind.size()<n) {    //아직 외울 공간이 충분할경우
	    		for(int j=0;j<mind.size();j++) {      //중복되는 경우 맨 뒤로 갱신해주고 시간 1초증가
		    		if(mind.get(j).equals(word.get(i))) {
		    			mind.remove(j);
		    			mind.add(word.get(i));
		    			res++;
		    			chk1=true;
		    			break;
		    		}
		    	}
	    		if(chk1==true)continue;
	    		mind.add(word.get(i));    //중복없으면 외울수 있는만큼 넣고 시간 3초 증가
	    		res+=3;
	
	    		continue;
	    	}
	    	else { 
	    		for(int j=0;j<mind.size();j++) {  //중복되는 경우 맨 뒤로 갱신해주고 시간 1초증가
		    		if(mind.get(j).equals(word.get(i))) {
		    			mind.remove(j);
		    			mind.add(word.get(i));
		    			res++;
		    			chk2=true;
		    			break;
		    		}
		    	}
	    		if(chk2==true)continue;
	    		
	    		int sum=0;
	    		for(int k=0;k<n;k++) { //문자열 평균길이 계산
	    			sum+=mind.get(k).length();
	    		}
	    		sum/=n;
	    		for(int k=0;k<n;k++) { //중복없으면 문자열이 평균보다 긴것 다음으로 오래된 단어 제거하고 그냥 넣고 시간3초증가
	    			if(mind.get(k).length()<=sum) {
	    				mind.add(word.get(i));
	    				mind.remove(k);	    				
	    				res+=3;
	    				
	    				break;
	    			}
	    		}
	    	}
	    	
	      }
	    
	    System.out.println(res);
	    
	    
	}

}
