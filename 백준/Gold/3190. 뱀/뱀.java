import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int k = Integer.parseInt(br.readLine());

        Set<String> apple_lst = new HashSet<>();
        for (int i = 0; i < k; i++) {
            String[] apple = br.readLine().split(" ");
            apple_lst.add(apple[0] + ","+apple[1]);
        }

        int l = Integer.parseInt(br.readLine());
        String[] direction_lst = new String[10001];
        for (int i = 0; i < l; i++) {
            String[] turnInfo = br.readLine().split(" ");
            int sec = Integer.parseInt(turnInfo[0]);
            direction_lst[sec] = turnInfo[1];
        }

        int[] dx = {-1, 0, 1, 0};
        int[] dy = {0, 1, 0, -1};

        int dr = 1;

        Deque<int[]> snake = new ArrayDeque<>();
        snake.addFirst(new int[]{1, 1});
        int ans = 0;

        while (true) {
            ans++;
            int[] head = snake.peekLast();
            int cx = head[0];
            int cy = head[1];
            int nx = cx + dx[dr];
            int ny = cy + dy[dr];

            if (1 <= nx && nx <= n && 1 <= ny && ny <= n && !isInSnake(snake, nx, ny)) {
                snake.addLast(new int[]{nx, ny});
                String pos = nx + "," + ny;
                if (apple_lst.contains(pos)) {
                    apple_lst.remove(pos);
                }
                else {
                    snake.removeFirst();
                }

                if ("D".equals(direction_lst[ans])) {
                    dr = (dr + 1) % 4;
                }
                else if ("L".equals(direction_lst[ans])) {
                    dr = (dr + 3) % 4;
                }


            }
            else {
                break;
            }

        }
        System.out.println(ans);
    }

    private static boolean isInSnake(Deque<int[]> snake, int x, int y) {
        for (int[] part : snake) {
            if (part[0] == x && part[1] == y){
                return true;
            }
        }
        return false;
    }

}
