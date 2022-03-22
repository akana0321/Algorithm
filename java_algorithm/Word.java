package java_algorithm;

import java.util.Scanner;

public class Word {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		//첫째 줄
		String[] first = scanner.nextLine().split(" ");
		
		//암기할 수 있는 수
		int n = Integer.parseInt(first[0]);
		
		//단어의 수
		int w = Integer.parseInt(first[1]);
		
		//둘째 줄
		String second = scanner.nextLine();
		
		//암기 배열
		String[] memory = new String[n];
		
		//단어 배열
		String[] word = new String[w];
		word = second.split(" ");		
		
		int sec = 0;				// 걸린 시간
		boolean check = false;		// 암기한 단어에 주어지는 단어가 있는지 판단
		int temp = 0;				// 암기한 단어의 위치 저장
		
		
		for(int i=0; i<w; i++) {			// 단어 목록을 처음부터 끝까지 순회
			check = false;					// 상태 초기화	
			// 단어를 암기했는지 체크
			for(int j=0; j<n; j++) {		// 암기한 단어를 순회
				// 머릿속에 단어가 있는지 체크
				if(memory[j] != null && memory[j].equals(word[i])) {	// memory에 단어가 있으면서 word[i]랑 같다면
					check = true;			// 이미 암기한 단어이므로 check1 = true
					temp = j;				// null인 공간에 word[i] 삽입
					break;					// for문 탈출
				}
			}
			
			// 암기 여부로 if문 수행
			if(check) {								// 암기한 단어면서 암기할 공간이 있는 경우
				sec += 1;							// 1초만에 대답
				for(int j=temp; j<n-1; j++) {		// 암기한 단어부터 시작해서 끝까지 순회
					if(memory[j+1] == null) {		// 암기한 단어 뒤가 비어있다면 가장 마지막 단어가 해당 단어 
						break;						// 가장 마지막 단어라는 뜻이므로 for문 탈출
					}
					memory[j] = memory[j+1];		// 한 칸씩 앞으로 당기기
		            if(j == n-2) {					// j번째 위치가 N-2인 경우 마지막 칸만 남아 있는 상태이므로
		            	memory[n-1] = word[i];		// 가장 마지막 위치에 word[i] 삽입
		            }
				}
			} else if(!check && memory[n-1] != null) {	// 암기하지 않은 단어면서 암기할 공간이 없는 경우
				sec += 3;							// 암기하지 않은 단어이므로 3초가 걸림
	            int lengthSum = 0;					// 단어 전체 길이를 저장하는 변수
	            int lengthAvg = 0;					// 단어 전체 길이의 평균
	            for(int j=0; j<n; j++) {			// 외우고 있는 단어를 순회
	               lengthSum += memory[j].length();	// 단어의 길이를 더함
	            }
	            lengthAvg = lengthSum / n;			// 단어 길이의 평균 계산
	            
	            for(int j=0; j<n-1; j++) {			// 다시 암기한 단어를 순회하면서
	               if(memory[j].length() <= lengthAvg) {	// 만약 암기한 단어의 길이가 평균보다 작거나 같으면
	                  for(int k=j; k<n-1; k++) {	// 해당 단어부터 암기한 단어 끝까지 다시 순회를 하고
	                	  memory[k] = memory[k+1];	// 하나씩 앞으로 당김
	                  }
	                  memory[n-1] = word[i];		// 암기한 단어의 마지막에 주어진 단어를 저장
	                  break;						// for문 탈출
	               }
	            }							
			} else { 							// 모르는 단어지만 외울 공간이 남아있는 경우
	            for(int j = 0; j<n; j++) {		// 외운 공간을 끝까지 순회
	            	if(memory[j] == null) {		// 빈공간을 찼았다면
	            		memory[j] = word[i];	// 삽입
	            		sec += 3;				// 대답 3초
	            		break;
	            	}
	            }
	         }
		}
		
		System.out.println("걸린 시간을 초단위로 출력\n");
		System.out.println(sec);
	}
}
