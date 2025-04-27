package java_algorithm;

import java.util.*;

public class Athlete {
	public String solution(String[] participant, String[] completion) {
        String answer = "";
        
        HashMap<String, Integer> map = new HashMap<>();	// <이름, 카운트> 쌍의 Map
        for(String p : participant) {
        	if(map.containsKey(p)) {
        		map.replace(p, map.get(p) + 1);	// 이름이 같은 사람이 있으면 숫자 +1
        	} else {
        		map.put(p, 1);		// 처음 본 이름이라면 1로 설정
        	}
        }
        
        for(String c : completion) {
        	map.replace(c, map.get(c) - 1);	// 완주자에서 이름을 발견했다면 1을 뺌
        }
        
        for(String s : map.keySet()) {	//key값을 하나씩 거내서
        	if(map.get(s) == 1) {		// 해당 이름에 해당하는 값이 1이라면(완주한 목록에 없음)
        		answer = s;				// 완주하지 못한사람
        		break;
        	}
        }
        
        return answer;
    }
}
