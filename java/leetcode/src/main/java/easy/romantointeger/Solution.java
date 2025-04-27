package easy.romantointeger;

public class Solution {
    public int romanToInt(String s) {
        int result = 0;

        // 뒤에서부터 순회
        int index = s.length() - 1;
        while (index > -1) {
            int current = this.getNumberByRomanWord(s.charAt(index));
            int next = index > 0 ? this.getNumberByRomanWord(s.charAt(index - 1)) : Integer.MAX_VALUE;

            if (current > next) {
                result += (current - next);
                index--;
            } else {
                result += (current);
            }

            index--;
        }

        return result;
    }

    private int getNumberByRomanWord (char word) {
        int number = 0;

        switch (word){
            case 'I':
                number = 1;
                break;
            case 'V':
                number = 5;
                break;
            case 'X':
                number = 10;
                break;
            case 'L':
                number = 50;
                break;
            case 'C':
                number = 100;
                break;
            case 'D':
                number = 500;
                break;
            case 'M':
                number = 1000;
                break;
        }

        return number;
    }
}
