import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) throws Exception{
		// 입력 받기
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt(); // 책 개수
		int M = sc.nextInt(); // 한번 이동할 때 들 수 있는 최대 책 개수
		int arr[] = new int[N];
		for (int i = 0; i < N; i++) {
			arr[i] = sc.nextInt();
		}
		
		Arrays.sort(arr); // 내림차순 정렬
		// 음수만 담는 배열과 양수만 담는 배열 분리
		ArrayList<Integer> minus_arr = new ArrayList<Integer>();
		ArrayList<Integer> plus_arr = new ArrayList<Integer>();
		
		// 각 배열에 값 넣기
		for (int i = 0; i < N; i++) {
			if (arr[i]> 0) {
				plus_arr.add(arr[i]);
			}
			else {
				minus_arr.add(arr[i]);
			}
		}
		int minus_size = minus_arr.size();
		int plus_size = plus_arr.size();
		int idx = 0;  // 이 친구가 핵심 키임! 1이면 음수쪽이 큼, 2면 양수쪽이 큼, 한쪽에 값이 존재하지 않으면 0
		if (minus_arr.isEmpty() == false && plus_arr.isEmpty()== false) {
			if ((-1)*minus_arr.get(0) > plus_arr.get(plus_size-1)) {
				idx = 1; // 음수쪽의 젋댓값이 더 큰 경우
			}
			else {
				idx = 2; // 양수쪽의 절댓값이 더 큰 경우
			}
		}
		int count = 0; // 결괏값
		// 음수쪽 계산하기
		for (int i = 0; i < minus_size;i+=M) {
			if (idx == 1 || idx == 0) {
				count -= minus_arr.get(i);
				idx = -1;
			}
			else {
				count -= minus_arr.get(i)*2; 
			}
		}
		// 양수쪽 계산하기
		for (int i = plus_size-1; i > -1;i-=M) {
			if (idx == 2 || idx == 0) {
				count += plus_arr.get(i);
				idx = -1;
			}
			else {
				count += plus_arr.get(i)*2; 
			}
		}
		
		System.out.println(count);
	}
}