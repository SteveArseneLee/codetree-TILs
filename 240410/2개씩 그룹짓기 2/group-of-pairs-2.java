import java.io.*; import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());

        int[] arr = new int[2*n];
        for (int i = 0; i < 2*n; i++){

            int tmp = Integer.parseInt(st.nextToken());
            arr[i] = tmp;
        }
        Arrays.sort(arr);
        
        int ans = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++){
            int tmp_value = arr[n+i] - arr[i];
            
            ans = Math.min(ans, tmp_value);
        }
        bw.write(ans+"\n");

        br.close();         bw.flush();        bw.close();
    }
}