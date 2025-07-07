import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[][] board = new int[N][N];
        for (int i=0; i<N; i++) {
            board[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        }
        int maxlen = -1;
        int maxidx = -1;
        for (int ts = 0; ts<N; ts++) {
            Set<Integer> basket = new HashSet<>();
            for (int i = 0; i<5; i++) {
                for (int x = 0; x < N; x++) {
                    if (board[x][i] == board[ts][i] && x != ts) {
                        basket.add(x);
                    }
                }
            }
            if (maxlen < basket.size()) {
                maxlen = basket.size();
                maxidx = ts;
            }
        }
        System.out.println(maxidx+1);
    }
    public static void stringPrinter(List<Long> list) {
        StringJoiner joiner = new StringJoiner(" ");
        for (Object n : list) {
            joiner.add(n.toString());
        }
        System.out.println(joiner.toString());
    }
}