package easy.longestcommonprefix;

public class Solution {
		public String longestCommonPrefix(String[] strs) {
			// 전달받은 목록이 없을 경우 공백을 반환한다.
			if (strs == null || strs.length < 1) {
				return "";
			}

			// 첫번째 항목 기준으로 문자열을 비교한다.
			for (int i = 0; i < strs[0].length(); i++) {
				char c = strs[0].charAt(i);

				// 첫번재 항목 이외의 항목을 비교한다.
				for (int j = 1; j < strs.length; j++) {
					// i가 비교 대상 문자열의 길이보다 크거나 i번째 문자가 다른 경우 i번째까지 substring하여 반환한다.
					if (i >= strs[j].length() || strs[j].charAt(i) != c) {
						return strs[0].substring(0, i);
					}
				}
			}

			// for문을 모두 순회하고 나왔을 경우는 strs[0]를 구성한 문자가 모두 prefix인 경우이다.
			return strs[0];
		}
}
