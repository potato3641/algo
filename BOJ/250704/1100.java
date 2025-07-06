import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int answer = 0;
        for (int i = 0; i < 8; i++) {
            String line = sc.nextLine();
            int idx = 0;
            while (idx < 8 && idx >= 0) {
                idx = line.indexOf("F", idx);
                if (idx == -1) {
                    break;
                }
                if (idx%2 == i%2) {
                    answer++;
                }
                idx++;
            }
        }
        System.out.println(answer);
    }
}