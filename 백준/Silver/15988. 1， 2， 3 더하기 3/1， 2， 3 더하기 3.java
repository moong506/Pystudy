import java.util.Scanner;


public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        int[] arr = new int[T];

        for(int i = 0; i < T; i++) {
            arr[i] = sc.nextInt();
        }
        double[] ans = new double[1000001];
        ans[1] = 1;
        ans[2] = 2;
        ans[3] = 4;
        for(int j = 4; j < 1000000+1; j++){
            ans[j] = (ans[j-1]+ans[j-2]+ans[j-3]) % 1000000009;
        }
        for(int i = 0; i < T; i++){
            System.out.println((int) ans[arr[i]]);
        }

    }




   }