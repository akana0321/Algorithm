package java_algorithm;

import java.util.*;

public class Spy {
	public static int solution(String[][] clothes) {
        int answer = 1;
        
        Map<String, Integer> hs = new HashMap<>();
        for(String[] sa : clothes) {
        	// sa[1]은 옷의 타입
        	if(hs.containsKey(sa[1])) {	// 해당 옷의 종류가 있다면
        		hs.replace(sa[1], hs.get(sa[1]) + 1);	// 개수 +1
        	} else {
        		hs.put(sa[1], 1);		// 없으면 1을 기본으로 줌
        	}
        }
        
        Iterator<String> iterator = hs.keySet().iterator();
        while(iterator.hasNext()) {	// 처음부터 끝까지 순회하면서
        	answer *= (hs.get(iterator.next())+1);	// 경우의 수를 곱해줌
        }
        // 아무것도 안입는 경우를 제외해야 하므로 1을 빼서 리턴
        return answer - 1;
    }
	
	public static void main(String[] args) {
		String[][] clothes = {{"yellowhat", "headgear"}, {"bluesunglasses", "eyewear"}, {"green_turban", "headgear"}};
		System.out.println(solution(clothes));
	}
}
