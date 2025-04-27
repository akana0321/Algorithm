package java_algorithm;

import java.util.Scanner;

public class Word1 {

	public static void main(String[] args) {
	      // TODO Auto-generated method stub
	      int num = 0;           //암기할 수 있는 수
	      int wordsNum = 0;      //암기해야할 단어의 수
	      int time =0;          //걸린 시간
	      
	      Scanner sc = new Scanner(System.in);

	      //1. 암기할수있는 수와 암기해야할 단어의 수 입력받음
	      String str = sc.nextLine();
	      String [] array = str.split(" ");
	      int [] intArray = new int[array.length];
	      for(int i=0; i<intArray.length; i++) {
	         intArray[i]=Integer.parseInt(array[i]);
	      }
	      num = intArray[0];                 //암기할 수 있는 수
	      wordsNum = intArray[1];             //단어의 수
	      String [] myWords = new String[num];   //머릿속
	      String [] words = new String[wordsNum]; //입력받을 단어 리스트

	      
	      //2. 영어 단어 리스트 입력받음
	      str = sc.nextLine();
	      words = str.split(" ");

	      //3. 걸린 시간 계산 
	      int emptyNum = num;       //머리에 몇개의 단어를 암기할 수 있는지를 나타내는 변수
	      int emptyIndex = 0;       //빈곳의 인덱스를 저장하는 변수
	      int wordLengthSum =0;        //암기하고 있는 단어들의 길이 합
	      double wordLengthAvg = 0.0; //암기하고 있는 단어들의 평균 길이
	      
	      for(int i = 0; i<words.length; i++) {
	         if(emptyNum>0) {  //머리가 비어있으면 그 단어를 암기
	            myWords[emptyIndex] = words[i];
	            time+=3;
	            emptyNum--;
	            emptyIndex++;
	            wordLengthSum += words[i].length();
	            wordLengthAvg = (double)wordLengthSum / num;
	         }else {
	            for(int j=0; j<myWords.length; j++) {
	               if(words[i].equals(myWords[j])) {  //머릿속에 있다면
	                  time+=1;
	                  for(int k =j+1; k<myWords.length; k++) {  //해당 단어의 암기 시점을 최신으로
	                     myWords[k-1] = myWords[k];
	                  }
	                  myWords[myWords.length-1] = words[i];
	                  break;
	               }else {  //머릿속에 없다면
	                  
	                  time+=3;
	                  int c =0; //지울 인덱스  //0
	                  for(int u =0; u<myWords.length;u++) {
	                     c=u;
	                     if(myWords[u].length()<wordLengthAvg) {
	                        break;
	                     }
	                  }
	                  wordLengthSum-=myWords[c].length();
	                  wordLengthSum += words[i].length();
	                  wordLengthAvg = (double)wordLengthSum / num;
	                  myWords[c] = words[i];

	                  break;
	               }
	            }
	         }

	      }
	      System.out.println("\n걸린 시간을 초단위로 출력\n");
	      System.out.println(time);
	   }



}
