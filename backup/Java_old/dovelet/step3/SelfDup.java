package dovelet.step3;

public class SelfDup {
	public static void main(String[] args) {
		for(int i=1; i<=10000; i++) {
			String strI = String.valueOf(i);
			String strPowI = String.valueOf((int)Math.pow(i, 2));
			if(strI.equals(strPowI.substring(strPowI.length()-strI.length(), strPowI.length())))
				System.out.println(i);
		}
	}
}
