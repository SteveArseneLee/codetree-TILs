import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static final int MAX_N = 100;
    public static final int DIR_NUM = 4;

    public static int n, t;
    public static int x, y, dir;
    public static int ans;
    public static String str;
    public static int[][] board = new int[MAX_N][MAX_N];

    public static int[] dx = new int[]{-1, 0, 1,  0};
    public static int[] dy = new int[]{ 0, 1, 0, -1};

    public static boolean inRange(int x, int y) {
        return 0 <= x && x < n && 0 <= y && y < n;
    }

    public static void simulate() {
        for(int i = 0; i < t; i++) {
            // R 명령이 나올 경우 방향을 오른쪽으로 바꿔줍니다.
            if(str.charAt(i) == 'R')
                dir = (dir + 1) % 4;
            // L 명령이 나올 경우 방향을 왼쪽으로 바꿔줍니다.
            else if(str.charAt(i) == 'L')
                dir = (dir + 3) % 4;
            // 해당 방향으로 움직입니다.
            else {
                int nx = x + dx[dir];
                int ny = y + dy[dir];
                // 이동할 수 있는 칸이면 이동합니다.
                // 해당 칸 안에 있는 숫자를 정답에 더해줍니다.
                if(inRange(nx, ny)) {
                    ans += board[nx][ny];
                    x = nx;
                    y = ny;
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        // 입력
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        t = Integer.parseInt(st.nextToken());
        str = br.readLine();

        for(int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < n; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // 초기 시작 위치를 설정합니다.
        x = n / 2;
        y = n / 2;
        dir = 0;

        ans += board[x][y];

        simulate();

        // 정답을 출력합니다.
        System.out.print(ans);
    }
}