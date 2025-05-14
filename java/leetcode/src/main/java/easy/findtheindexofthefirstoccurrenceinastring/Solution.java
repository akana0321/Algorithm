package easy.findtheindexofthefirstoccurrenceinastring;

/**
 * Find The Index Of The First Occurrence In A String
 * https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string
 */
public class Solution {
	public int strStr(String haystack, String needle) {
		int startIndex = -1;

		// 전달받은 인자가 비어있을 경우 함수를 종료한다.
		if (haystack.isEmpty() || needle.isEmpty()) {
			return startIndex;
		}

		// 찾을 문자열이 포함되어 있지 않을 경우 -1을 반환한다.
		if (!haystack.contains(needle)) {
			return startIndex;
		}

		// 찾을 문자열이 더 긴 경우 -1을 반환한다.
		if (needle.length() > haystack.length()) {
			return startIndex;
		}

		// 찾을 문자열의 첫번째 문자
		char firstNeedleChar = needle.charAt(0);
		for (int i = 0; i < haystack.length(); i++) {
			// 찾을 문자열의 첫번째 문자로 시작하지 않는 경우 다음 반복문으로 넘어간다.
			if (haystack.charAt(i) != firstNeedleChar) {
				continue;
			}

			// 시작 index를 i번째로 한다.
			startIndex = i;
			// 문자열을 시작지점부터 마지막까지 substring 한다.
			String substringHaystack = haystack.substring(i);
			// 포함여부 플래그
			boolean isContain = true;

			// 시작 다음지점부터 찾을 문자열이 같은지 확인한다.
			for (int j = 1; j < needle.length(); j++) {
				// 둘의 문자가 다를 경우
				if (substringHaystack.charAt(j) != needle.charAt(j)) {
					// 포함여부를 false로 한다.
					isContain = false;
					// 시작 Index를 초기화한다.
					startIndex = -1;
					break;
				}
			}

			if (isContain) {
				break;
			}
		}

		return startIndex;
	}
}
