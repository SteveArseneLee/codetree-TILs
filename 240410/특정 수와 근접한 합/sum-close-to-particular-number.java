import java.io.*;
import java.util.*;

public class Main{
    public static final int INT_MAX = Integer.MAX_VALUE;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int S = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int[] arr = new int[n];
        int arr_Sum = 0;
        for (int i = 0; i<n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            arr_Sum += arr[i];
        }
        int ans = INT_MAX;

        for (int i = 0; i<n;i++){
            for (int j = i+1; j<n;j++){
               int newSum = arr_Sum - arr[i] - arr[j];

               int diff = Math.abs(newSum - S);
               ans = Math.min(ans, diff);
            }
        }
        bw.write(ans + "\n");
        bw.flush(); br.close(); bw.close();
    }
}