package java_algorithm;

import java.util.*;

public class FunctionDevelopment {
	public int[] solution(int[] progresses, int[] speeds) {
        int[] answer;
        List<Integer> result = new ArrayList<>(); // 결과 리스트 
        Queue<Integer> q = new LinkedList<>();	// 걸리는 시간 저장 큐
        
        // ( 100 - (현재 진행도) ) / (작업속도)를 올림한 값이 걸리는 기간
        for(int i=0; i < progresses.length; i++)
        	q.offer((int) Math.ceil((double) (100 - progresses[i]) / speeds[i]));
        
        while(!q.isEmpty()) {
        	int headDays = q.poll();	// 그 시점 현 프로세스 걸리는 기간을 뽑아냄
        	int finProgress = 1;		// 현 프로세스가 끝나는 시점에 완료되는 프로세스들
        	
        	// 큐가 비어있지 않고 현 프로세스가 끝나는 기간보다 작거나 같다면
        	while(!q.isEmpty() && headDays >= q.peek()) {
        		finProgress += 1;	// 완료되는 프로세스에 더함
        		q.poll();			// 큐에서 제거
        	}
        	result.add(finProgress);// 리스트에 추가
        }
        
        answer = new int[result.size()];	// 결과 배열
        for(int i=0; i<answer.length; i++)
        	answer[i] = result.get(i);		// 결과 배열에 결과 리스트값 저장
        
        return answer;
    }
	
	public static void main(String[] args) {
		FunctionDevelopment fd = new FunctionDevelopment();
		int[] answer = fd.solution(new int[] {95, 90, 99, 99, 80, 99}, new int[] {1, 1, 1, 1, 1, 1});
		System.out.println(); System.out.println();
		for(int i : answer)
			System.out.println(i);
	}
}
