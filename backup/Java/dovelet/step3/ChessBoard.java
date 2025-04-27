package dovelet.step3;

import java.io.*;
import java.util.*;

public class ChessBoard {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		
		int sequence = 1;
		while(2*sequence-1 < n)
			sequence++;
		
		System.out.println(sequence);
	}
}
