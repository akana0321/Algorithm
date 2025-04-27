package easy.palindromenumber;

/**
 * palindrome number
 * https://leetcode.com/problems/palindrome-number/solutions/3213890/fastest-java-solution/?difficulty=EASY
 */
public class Solution {
    public boolean isPalindrome(int x) {
        // 음수일 경우 해당하지 않음
        // ex) -121 <-> 121- -> false
        if  (x < 0) {
            return false;
        }

        // 문자열로 변경한다.
        String xString = Integer.toString(x);
        int xStringLength = xString.length();

        for (int i = 0; i < xStringLength - 1; i++) {
            // 양 끝이 다를 경우 false 반환
            if (xString.charAt(i) != xString.charAt(xStringLength - 1 - i)) {
                return false;
            }
        }

        return true;
    }
}
