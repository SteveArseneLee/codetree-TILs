import java.io.*; import java.util.*;
public class Main{
    public static final int MAX_VAL = 10000;
    public static int[] arr = new int[MAX_VAL+1];

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        // n명의 사람들에 대한 정보 입력
        for (int i = 0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            String c = st.nextToken();

            if (c.equals("G")) arr[x] = 1;
            else arr[x] = 2;
        }

        // 모든 시작점 잡아보기
        int maxSum=0;
        for (int i = 0; i <= MAX_VAL -k ; i++){
            int sumVal = 0;
            for (int j = i; j<= i+k;j++)
                sumVal += arr[j];
            maxSum = Math.max(maxSum, sumVal);
        }
        bw.write(maxSum + "\n"); bw.flush(); br.close(); bw.close();
    }
}