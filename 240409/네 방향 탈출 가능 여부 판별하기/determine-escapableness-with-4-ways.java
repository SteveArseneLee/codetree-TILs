import java.util.Scanner;
import java.util.Queue;
import java.util.ArrayDeque;
class Pair {
    int x, y;
    public Pair(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class Main {
    public static final int MAX_NUM = 100;

    public static int n, m;
    public static int[][] a = new int[MAX_NUM][MAX_NUM];

    // bfs에 필요한 변수들 입니다.
    public static boolean[][] visited = new boolean[MAX_NUM][MAX_NUM];
    public static Queue<Pair> q = new ArrayDeque<>();

    public static boolean inRange(int x, int y) {
        return 0 <= x && x < n && 0 <= y && y < m;
    }

    public static boolean canGo(int x, int y) {
        return inRange(x, y) && a[x][y] == 1 && !visited[x][y];
    }

    public static void BFS() {
        // queue에 남은 것이 없을때까지 반복합니다.
        while(!q.isEmpty()) {
            // queue에서 가장 먼저 들어온 원소를 뺍니다.
            Pair curr = q.poll();
            int x = curr.x, y = curr.y;

            int[] dx = new int[]{0, 1,  0, -1};
            int[] dy = new int[]{1, 0, -1,  0};

            // queue에서 뺀 원소의 위치를 기준으로 4방향을 확인해봅니다.
            for(int i = 0; i < 4; i++) {
                int newX = x + dx[i];
                int newY = y + dy[i];

                // 아직 방문한 적이 없으면서 갈 수 있는 곳이라면
                // 새로 queue에 넣어주고 방문 여부를 표시해줍니다.
                if(canGo(newX, newY)) {
                    q.add(new Pair(newX, newY));
                    visited[newX][newY] = true;
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 입력
        n = sc.nextInt();
        m = sc.nextInt();
        for(int i = 0; i < n; i++)
            for(int j = 0; j < m; j++)
                a[i][j] = sc.nextInt();

        // bfs를 이용해 최소 이동 횟수를 구합니다.
        // 시작점을 queue에 넣고 시작합니다.
        q.add(new Pair(0, 0));
        visited[0][0] = true;

        BFS();

        // 우측 하단을 방문한 적이 있는지 여부를 출력합니다.
        int answer = visited[n - 1][m - 1] ? 1 : 0;
        System.out.println(answer);
    }
}