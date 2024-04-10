import java.io.*; import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int[] arr = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i<n;i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        // i번째가 와이파이 위치면 i-n~i+n까지 사람들이 사용가능.
        int cnt = 0;
        for (int i = 0; i<n;i++){
            if (arr[i] == 1){
                cnt++;
                i += 2*m;
            }
        }
        bw.write(cnt + "\n");


        br.close();         bw.flush();        bw.close();
    }
}