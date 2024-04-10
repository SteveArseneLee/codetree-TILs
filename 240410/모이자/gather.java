import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;
public class Main{
    public static final int INT_MAX = Integer.MAX_VALUE;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int[] arr = new int[n];
        st = new StringTokenizer(br.readLine()," ");
        for (int i = 0; i<n;i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }
//        System.out.print(n);
        int ans = INT_MAX;
        for (int i=0;i<n;i++) {
            int tmp = 0;
            for (int j = 0; j < n; j++) {
                tmp += Math.abs(i-j) * arr[j];
            }
            ans = Math.min(ans, tmp);
        }
        bw.write(ans + "\n");
        bw.flush(); br.close(); bw.close();
    }
}