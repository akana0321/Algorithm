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

		// 전달받은 문자열의 마지막 단어의 끝
		int endOfLastWord = s.length() - 1;
		// 문자열의 마지막부터 공백인 경우 하나씩 줄여나간다.(공백이 아닐 때까지 반복)
		while (endOfLastWord >=0 && s.charAt(endOfLastWord) == ' ') {
			endOfLastWord--;
		}

		// 시작지점을 마지막 단어의 끝으로 한다.
		int startOfLastWord = endOfLastWord;
		// 마지막 지점부터 공백이 아닌 경우 하나씩 줄여나간다(공백을 만날 때까지 반복)
		while (startOfLastWord >= 0 && s.charAt(startOfLastWord) != ' ') {
			startOfLastWord--;
		}

		// 마지막 지점 - 시작 지점 = 단어의 길이
		return endOfLastWord - startOfLastWord;
	}
}
