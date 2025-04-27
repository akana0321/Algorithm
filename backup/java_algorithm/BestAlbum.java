package java_algorithm;

import java.util.*;

class Song implements Comparable<Song>  {
	String genre;
	int play;
	int originNum;
	
	public Song(String genre, int play, int originNum) {
		this.genre = genre;
		this.play = play;
		this.originNum = originNum;
	}
	
	@Override
	public int compareTo(Song o) {
		return (o.play - this.play);
	}	
}

public class BestAlbum {
	public int[] solution(String[] genres, int[] plays) {
        int[] answer;
        HashMap<String, Integer> hm = new HashMap<>();	// 각 장르별 최고 재생횟수 저장 map
        for(int i=0; i<genres.length; i++) {        	
        	if(hm.containsKey(genres[i]))				// 장르별 재생횟수 저장
        		hm.replace(genres[i], hm.get(genres[i]) + plays[i]);
        	else
        		hm.put(genres[i], plays[i]);
        }
        
        // 1. 최고 재생횟수 순으로 장르 저장
        List<String> mostGenres = new ArrayList<>();
        while(hm.size() != 0) {
        	String mostGenre = "";				// 현 시점 최고 장르
        	int mostPlay = -1;					// 현 시점 최대 재생 횟수
        	for(String key : hm.keySet()) {
        		if(mostPlay < hm.get(key)) {	// 계속 비교하면서 갱신함
        			mostGenre = key;
        			mostPlay = hm.get(key);
        		}
        	}
        	mostGenres.add(mostGenre);			// mostGenres에 추가
        	hm.remove(mostGenre);				// 해당 장르를 HashMap에서 제거
        }
        
        // 2. 장르 별 베스트앨범 수록곡 뽑기
        ArrayList<Integer> result = new ArrayList<>();	// 결과 리스트
        for(String mostGenre : mostGenres) {			// 최고 장르부터 시작해서
        	List<Song> list = new ArrayList<>();		// 노래 목록을 저장하는 리스트
        	for(int i=0; i<genres.length; i++) {
        		if(genres[i].equals(mostGenre)) {		// 만약 현 시점 최고 장르라면
        			list.add(new Song(genres[i], plays[i], i));	// 저장
        		}
        	}
        	Collections.sort(list);						// 재생 횟수 기준으로 내림차순 정렬
        	
        	result.add(list.get(0).originNum);			// 최고 장르 중 가장 많이 재생된 곡의 고유 번호 삽입
        	if(list.size() >= 2) {						// 한 곡만 있을 수도 있으므로 2개 이상일 경우만
        		result.add(list.get(1).originNum);		// 두 번째 곡도 저장
        	}
        }
        
        answer = new int[result.size()];
        for(int i=0; i<answer.length; i++) {
        	answer[i] = result.get(i);
        }
        return answer;
    }
}
