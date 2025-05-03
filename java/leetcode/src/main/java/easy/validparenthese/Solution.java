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

		// 괄호 Deque
		Deque<Character> bracketsDeque = new ArrayDeque<>();
		// 괄호 쌍
		Map<Character, Character> bracketPairs = Map.of(
						'(', ')',
						'{', '}',
						'[', ']'
		);

		for (char current : s.toCharArray()) {
			if (bracketPairs.containsKey(current)) {
				// 여는 괄호일 경우 Deque에 담는다.
				bracketsDeque.push(bracketPairs.get(current));
			} else if (bracketPairs.containsValue(current)) {
				// 닫는 괄호일 경우 Deque.pop() 값과 일치하지 않을 경우 false를 반환한다.
				if (bracketsDeque.isEmpty() || bracketsDeque.pop() != current) {
					return false;
				}
			} else {
				// 이외의 값이 들어올 결우 false를 반환한다.
				return false;
			}
		}

		return bracketsDeque.isEmpty();
	}
}
