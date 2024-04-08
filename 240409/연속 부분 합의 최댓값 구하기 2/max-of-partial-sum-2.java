import java.util.Scanner;

public class Main {    
    public static int INT_MIN = Integer.MIN_VALUE;
    public static final int MAX_N = 100000;
    
    // 변수 선언
    public static int n;
    public static int[] a = new int[MAX_N + 1];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // 입력:
        n = sc.nextInt();
        for(int i = 1; i <= n; i++)
            a[i] = sc.nextInt();

        // 최댓값을 구해야 하는 문제이므로
        // 초기값을 INT_MIN으로 설정합니다.
        int ans = INT_MIN;

        // 현재 연속 부분 수열 내 원소의 합을
        // 저장합니다.
        int sum = 0;

        for(int i = 1; i <= n; i++) {
            // 만약 현재 연속 부분 수열 내 원소의 합이
            // 0보다 작아진다면, 지금부터 새로운
            // 연속 부분 수열을 만드는 것이 더 유리합니다.
            if(sum < 0)
                sum = a[i];
            
            // 그렇지 않다면 기존 연속 부분 수열에 
            // 현재 원소를 추가하는 것이 더 좋습니다.
            else
                sum += a[i];
            
            // 가능한 연속 부분 수열 중 최댓값을 찾아 갱신합니다.
            ans = Math.max(ans, sum);
        }
        
        System.out.print(ans);
    }
}