import java.util.Scanner;
import java.util.HashMap;

public class Main {    
    // 변수 선언
    public static int n;
    public static HashMap<Integer, Integer> m = new HashMap<>();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // 입력:
        n = sc.nextInt();
        
        for(int i = 0; i < n; i++) {
            String command = sc.next();

            if(command.equals("add")) {
                int k = sc.nextInt();
                int v = sc.nextInt();
                m.put(k, v);
            }
            else if(command.equals("remove")) {
                int k = sc.nextInt();
                m.remove(k);
            }
            else {
                int k = sc.nextInt();
                if(!m.containsKey(k))
                    System.out.println("None");
                else
                    System.out.println(m.get(k));
            }
        }
    }
}