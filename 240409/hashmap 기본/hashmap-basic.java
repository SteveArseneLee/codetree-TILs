import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.HashMap;
import java.io.IOException;
import java.util.StringTokenizer;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;

public class Main{
    public static void main(String[] args) throws IOException{
        HashMap<Integer, Integer> m = new HashMap<>();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        for (int i = 0; i<n;i++){
            st = new StringTokenizer(br.readLine());
            String command = st.nextToken();

            if (command.equals("add")){
                int k = Integer.parseInt(st.nextToken());
                int v = Integer.parseInt(st.nextToken());
                m.put(k,v);
            } else if (command.equals("remove")){
                int k = Integer.parseInt(st.nextToken());
                m.remove(k);
            } else{
                int k = Integer.parseInt(st.nextToken());
                if (!m.containsKey(k))
                    bw.write("None" + "\n");
                else
                    bw.write(m.get(k) + "\n");
            }

        }
        bw.flush();
        br.close();
        bw.close();
    }
}