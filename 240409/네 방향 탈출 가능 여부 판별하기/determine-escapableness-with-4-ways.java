import java.io.IOException;
import java.util.ArrayDeque;
import java.util.Queue;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

class Pair{
    int x,y;
    public Pair(int x, int y){
        this.x = x;
        this.y = y;
    }
}
public class Main{
    public static final int MAX_NUM = 100;
    public static int n,m;
    public static int[][] grid = new int[MAX_NUM][MAX_NUM];
    public static boolean[][] visited = new boolean[MAX_NUM][MAX_NUM];
    public static Queue<Pair> q = new ArrayDeque<>();

    public static boolean inRange(int x, int y){
        return 0<=x && x<n && 0<=y && y<m;
    }
    public static boolean canGo(int x, int y){
        return inRange(x,y) && grid[x][y] == 1 && !visited[x][y];
    }

    public static void BFS(){
        while(!q.isEmpty()){
            // queue에서 가장 먼저 들어온 원소 뽑기
            Pair curr = q.poll();
            int x = curr.x, y=curr.y;

            int[] dx = new int[]{0,1,0,-1};
            int[] dy = new int[]{1,0,-1,0};

            // queue에서 4방향 보기
            for (int i = 0; i<4;i++){
                int newX = x + dx[i];
                int newY = y + dy[i];

                if (canGo(newX, newY)){
                    q.add(new Pair(newX, newY));
                    visited[newX][newY] = true;
                }
            }
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        for(int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < m; j++) {
                grid[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        q.add(new Pair(0, 0));
        visited[0][0] = true;
        BFS();

        int answer = visited[n - 1][m - 1] ? 1 : 0;
        bw.write(answer + "\n");
        bw.flush();
        br.close();
        bw.close();
    }
}