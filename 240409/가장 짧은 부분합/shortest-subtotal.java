import java.io.*;
import java.util.*;

public class Main{
    public static final int MAX_N = 100000;
    public static final int INT_MAX = Integer.MAX_VALUE;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int s = Integer.parseInt(st.nextToken());
        int[] arr = new int[MAX_N];
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= n; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int ans = INT_MAX;

        int sumVal = 0;
        int j = 0;
        for (int i = 1;i<=n;i++){
            while ( j <=n && sumVal < s){
                sumVal += arr[j+1];
                j++;
            }

            if (sumVal < s)
                break;
            ans = Math.min(ans, j-i+1);

            sumVal -= arr[i];
        }

        if (ans == INT_MAX)
            ans = -1;
        bw.write(ans + "\n");

        bw.flush();
        br.close();
        bw.close();
    }
}