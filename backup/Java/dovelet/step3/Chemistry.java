package dovelet.step3;

import java.io.*;
import java.util.*;

public class Chemistry {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		List<Float> results = new ArrayList<>();
		float first = Float.parseFloat(br.readLine());
		float second = 0;
		
		while(true) {
			second = Float.parseFloat(br.readLine());
			if(second == 999)
				break;
			else
				results.add(second-first);
			first = second;
		}
		
		for(int i=0; i<results.size(); i++)
			System.out.printf("%.2f\n", results.get(i));
		System.out.println("End of Output");
	}
}
