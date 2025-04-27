package java_algorithm;
/*
 * 다리를 지나는 트럭(https://programmers.co.kr/learn/courses/30/lessons/42583?language=java)
 */
import java.util.*;

public class PassingTruck {
	public static int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        int now = 0;	// 현재 다리의 무게
        
        // 다리를 의미하는 큐
        Queue<Integer> q = new LinkedList<>();
        
        for(int tw : truck_weights) {
        	while(true) {
        		// 다리가 비어있는 경우
            	if(q.isEmpty()) {
            		q.offer(tw);  // 트럭 추가
            		now += tw;	  // 현재 무게에 추가
            		answer += 1;  // 1초 추가
            		break;
            	// 다리의 길이만큼 트럭이 올라와 있는 경우
            	} else if(q.size() == bridge_length) {
            		// 1초에 1대만 빠질 수 있음
            		now -= q.poll();
            	// 다리 위에 트럭이 있는 경우
            	} else {
            		// 다리가 견딜 수 있는 무게보다 현재 트럭들의 무게가 더 커서 추가할 수 없다면
            		if(weight < now + tw) {
            			answer += 1;	// 1초 추가
            			// 트럭이 올라와있는 수를 맞추기 위해 0을 삽입
            			q.offer(0);
            		} else {
            			// 다리가 견딜 수 잇는 무게보다 현재 트럭들의 무게가 더 적은 경우
            			q.offer(tw);	// 다리 위에 트럭 올리기
            			now += 1;		// 현재 무게에 추가
            			answer += 1;	// 1초 추가
            			break;
            		}
            	}
        	}
        }
        // 트럭마다의 나가는 시간의 합 + 다리의 길이가 총 걸린 시간
        return (answer + bridge_length);
    }
	
	public static void main(String[] args) {
		int bridge_length = 2;
		int weight = 10;
		int[] truck_weights = {7,4,5,6};
		System.out.println(solution(bridge_length, weight, truck_weights));
	}
}
