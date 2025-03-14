import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Queue;
import java.util.LinkedList;


public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); //Scanner 보다 빠름
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N, M;
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        int [][] box = new int[N][M];
        Queue<int[]> queue = new LinkedList<>();
        for (int i = 0; i < N; i++){
            st = new StringTokenizer(br.readLine(), " ");
            for (int j = 0; j < M; j++){
                box[i][j] = Integer.parseInt(st.nextToken());
                if (box[i][j] == 1){  // 시작점이 여러개이므로 미리 queue에 넣어놓기
                    queue.add(new int[] {i, j});
                }
            }
        }
        int days = 0;
        if (!isAllRipe(box)) {
        	days = bfs(N, M, queue, box);
        }
        
        System.out.print(days);

        
	}
	static boolean isAllRipe(int[][] box) {
		for (int i = 0; i<box.length;i++) {
        	for (int j = 0; j < box[i].length; j++) {
        		if (box[i][j] == 0) {
        			return false;
        		}
        	}
        }
		return true;
	}
	static int bfs(int N, int M, Queue<int[]> queue, int[][] box){
        int days = 0;
        int[][] visited = new int[N][M];
        int[][] delta = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}};
        
        while(!queue.isEmpty()){
        	int[] temp = queue.poll();
        	int ti = temp[0];
        	int tj = temp[1];
        	for (int[] d : delta ) {
        		int ni = ti + d[0];
        		int nj = tj + d[1];
        		if (0<= ni && ni < N && 0<=nj && nj <M && box[ni][nj] == 0) {
        			visited[ni][nj] = visited[ti][tj] + 1;
        			box[ni][nj] = 1;
        			queue.add(new int[] {ni, nj});
        		}
        	}
        }
        
        for (int i = 0; i<N;i++) {
        	for (int j = 0; j < M; j++) {
        		if (box[i][j] == 0) {
        			days = -1;
        			break;
        		}
        		if (visited[i][j]> days) {
        			days = visited[i][j];
        		}
        	}
        	if (days == -1) {
        		break;
        	}
        }
        return days;
    }
}

