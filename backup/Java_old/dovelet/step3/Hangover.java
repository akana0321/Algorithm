package dovelet.step3;

import java.io.*;

public class Hangover {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		double c = Double.parseDouble(br.readLine());
		int card = 1;
		double accumulate = 0.00;
		
		while(true) {
			card++;
			accumulate += (double)1/card;
			if(accumulate >= c) {
				System.out.println(card-1 + " card(s)");
				break;
			}
		}
	}
}
