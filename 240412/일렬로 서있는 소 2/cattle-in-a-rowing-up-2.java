import java.io.*; import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i<n;i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }
        int ans = 0;
        for (int i = 0; i<n;i++){
            for(int j = i+1; j<n;j++){
                for(int k = j+1; k<n;k++){
                    if ((arr[i] <= arr[j]) & (arr[j] <= arr[k])){
                        ans += 1;
                    }
                }
            }
        }
        System.out.print(ans);
    }
}