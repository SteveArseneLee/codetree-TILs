import java.io.*;

public class Main {
    public static final int MAX_N = 10000;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int[] blocks = new int[MAX_N];

        // n의 값 입력받음
        int n = Integer.parseInt(br.readLine());

        // 각 줄에서 하나의 숫자를 읽어 배열에 저장
        for (int i = 0; i < n; i++) {
            blocks[i] = Integer.parseInt(br.readLine());
        }

        // 전체 블럭 수 계산
        int sumOfBlocks = 0;
        for (int i = 0; i < n; i++)
            sumOfBlocks += blocks[i];

        // 평균 블럭 수 계산
        int avg = sumOfBlocks / n;
        int ans = 0;
        for (int i = 0; i < n; i++)
            if (blocks[i] > avg)
                ans += blocks[i] - avg;

        // 결과 출력
        bw.write(ans + "\n");

        // 리소스 해제
        br.close();
        bw.flush();
        bw.close();
    }
}