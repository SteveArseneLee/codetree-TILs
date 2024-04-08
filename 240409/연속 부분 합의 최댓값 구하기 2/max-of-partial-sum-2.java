import java.io.*;
import java.util.*;


// 부분 수열의 합이 최대가 될때의 값 출력
public class Main{
    public static int INT_MIN = Integer.MIN_VALUE;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int[] arr = new int[n];
        for (int i=0; i<n;i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }
//        System.out.print(Arrays.toString(arr));
        int ans = INT_MIN;
        int sum = 0;
        for (int i = 0; i<n;i++){
            if (sum < 0)
                sum = arr[i];
            else
                sum += arr[i];
            ans = Math.max(ans, sum);
        }
        bw.write(ans + "\n");

        bw.flush();
        br.close();
        bw.close();
    }
}