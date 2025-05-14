package easy.lengthoflastword;

/**
 * Length Of Last Word
 * https://leetcode.com/problems/length-of-last-word
 */
public class Solution {
	public int lengthOfLastWord(String s) {
		// 전달받은 문자열이 null이거나 공백일 경우 0을 반환한다.
		if (s == null || s.isEmpty()) {
			return 0;
		}

		// 전달받은 문자열의 앞, 뒤 공백을 제거한 후 공백으로 split한다.
		String[] splittedStrings = s.trim().split(" ");

		// split한 문자열의 마지막 번째의 길이를 반환한다.
		return splittedStrings[splittedStrings.length - 1].length();
	}
}
