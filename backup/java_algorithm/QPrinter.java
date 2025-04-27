package java_algorithm;

import java.util.*;

public class QPrinter {
	public int solution(int[] priorities, int location) {
        int answer = 0;
        // 내림차순 우선순위 큐 선언 및 대입
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for(int i=0; i<priorities.length; i++)
        	pq.offer(priorities[i]);
        
        // 우선순위 큐가 빌 때까지 또는 답이 도출될 때까지 반복
        while(!pq.isEmpty()) {
        	// 매개값으로 주어진 우선순위 배열과 우선순위 큐와 비교
        	for(int i=0; i<priorities.length; i++) {
        		// 만약 우선순위 배열과 우선순위 큐의 앞(우선순위가 높은 것)과 같다면
        		if(priorities[i] == pq.peek()) {
        			pq.poll();		// 큐에서 제거
        			answer += 1;	// 순번 + 1
        			// 만약 우선순위 배열의 위치와 요청한 문서의 위치가 같다면
        			if(location == i)
        				return answer;	// 바로 값을 리턴
        		}
        	}
        }
        return answer;
    }
	
	public static void main(String[] args) {
		HashMap<Integer, Integer> hm = new HashMap<>();
		hm.put(0, 1);
		hm.put(1, 4);
		hm.put(3, 1);
		hm.put(2, 2);
		hm.put(5, 5);
		
		ArrayList<Integer> keyList = new ArrayList<>(hm.keySet());
		Collections.sort(keyList, (o1, o2) -> (hm.get(o2) - hm.get(o1)));
		Iterator<Map.Entry<Integer, Integer>> iterator = hm.entrySet().iterator(); 
		while(iterator.hasNext()) {
			Map.Entry<Integer, Integer> entry = iterator.next();
			System.out.println(entry.getKey() + " : " + entry.getValue());
		}
		
		System.out.println();
		for(int i : keyList)
			System.out.println(i);
	}
}
