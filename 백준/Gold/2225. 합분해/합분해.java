import java.io.*;
import java.util.*;
public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int mod = 1000000000;

        int[][] dp = new int[k + 1][n + 1];
        for (int i = 0; i < n + 1; i++) {
            dp[1][i] = 1;
        }

        for (int i = 1; i <= k; i++) {
            dp[i][0] = 1;
        }

        for (int i = 2; i <= k; i++) {
            for (int j = 1; j < n + 1; j++) {
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % mod;
            }
        }

        System.out.println(dp[k][n] % mod);

    }
}
