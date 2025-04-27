package dovelet.step1;

import java.io.*;
import java.util.*;

public class KoiWatch {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int sec = 0;
		String[] strTimes = br.readLine().split(" ");
		int totalSec = Integer.parseInt(strTimes[0])*60*60
					  + Integer.parseInt(strTimes[1])*60
					  + Integer.parseInt(strTimes[2]);
		int cookTime = Integer.parseInt(br.readLine());
		totalSec += cookTime;
		
		if(totalSec >= 24*3600)
			totalSec %= 24*3600;
		
		strTimes[0] = String.valueOf(totalSec/3600);
		totalSec %= 3600;
		strTimes[1] = String.valueOf(totalSec/60);
		totalSec %= 60;
		strTimes[2] = String.valueOf(totalSec);
		
		System.out.println(strTimes[0] + " " + strTimes[1] + " " + strTimes[2]);
	}
}
