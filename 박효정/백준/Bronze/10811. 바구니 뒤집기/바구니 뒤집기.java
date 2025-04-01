import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt(); // 1 ~ N번 바구니
		int M = sc.nextInt(); // M번 교환 
		
		int[] arr = new int [N];
		for(int i=0; i<N; i++) {
			arr[i] = i+1;
		}
		
		for(int i=0; i<M; i++) {
			int s = sc.nextInt()-1; // 시작인덱스
			int e = sc.nextInt()-1; // 끝인덱스
			
			int v = (e-s)/2; // 바꿀 범위의 절반 
			
			for (int j=0; j<=v; j++) { // arr[s+1] <-> arr[e-1] 
				int tmp = arr[s+j];
				arr[s+j] = arr[e-j];
				arr[e-j] = tmp;
				
			}
			
		}
		
		for(int i=0; i<N; i++) {
			System.out.print(arr[i] + " ");
		}
		
	}
}
