package easy.validparenthese;

import java.util.*;

/**
 * Valid Parentheses
 * https://leetcode.com/problems/valid-parentheses/submissions/1624405570/
 */
public class Solution {
	public boolean isValid(String s) {
		// 전달받은 문자열의 길이가 0 또는 홀수일 경우 false를 반환한다.
		if (s.length() == 0 || s.length() % 2 == 1) {
			return false;
		}

		List<Character> brackets = new ArrayList<>();

		for (int i = 0; i < s.length(); i++) {
			char current = s.charAt(i);

			// 여는 괄호일 경우 닫는 괄호로 목록에 추가한다.
			if (current == '(') {
				brackets.add(')');
			} else if (current == '[') {
				brackets.add(']');
			} else if (current == '{') {
				brackets.add('}');
			} else {
				// 목록의 크기가 0일 경우 false를 반환한다.
				if (brackets.size() == 0) {
					return false;
				}

				// 목록의 마지막 괄호를 가져온다.
				char lastBracket = brackets.get(brackets.size() - 1);
				// 현재 괄호와 목록의 마지막 괄호가 다를 경우 false를 반환한다.
				if (current != lastBracket) {
					return false;
				}

				// 마지막 괄호를 제거한다.
				brackets.remove(brackets.size() - 1);
			}
		}

		// 문자열을 순회했는데 목록이 남았다면 false를 반환한다.
		if (brackets.size() != 0) {
			return false;
		}

		return true;
	}
}
