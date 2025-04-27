package java_algorithm;

import java.util.*;

public class PhoneBook {
	public boolean solution(String[] phone_book) {
        boolean answer = true;
        Arrays.sort(phone_book);	// 맨 앞의 숫자를 기준으로 정렬(1로 시작, 2로 시작....)
        for(int i=0; i<phone_book.length-1; i++) {
        	try {	// phone_book의 i번쨰가 i+1보다 클 수도 있기 때문에 try~catch 블록 생성
                // phone_book[i]와 phone_book[i+1]에서 0부터 phone_book[i]의 길이까지 잘라 같은지 비교
        		if(phone_book[i].equals(phone_book[i+1].substring(0, phone_book[i].length())))
                	return false;	// 같다면 false를 리턴
            } catch(Exception e) {
                continue;			// 오류가 나는 경우 다음 for문으로 넘어감
            }
        }    
        return answer;				// 여기까지 온 것은 접두사로 시작하는 것이 없다는 것이므로 true 리턴
    }
	
	public static void main(String[] args) {
		String s = "abcdefg";
		System.out.println(s.substring(0, s.length()));
		
		String[] ss = {"11", "123", "56654", "1", "8754", "234"};
		Arrays.sort(ss);
		for(String k : ss) 
			System.out.println(k);
	}
}
