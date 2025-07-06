import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Integer> list = Arrays.asList(sc.nextInt(), sc.nextInt(), sc.nextInt(), sc.nextInt(), sc.nextInt());
        int min = Collections.min(list);
        while (true) {
            int cnt = 0;
            for (Integer e : list) {
                if (min%e == 0) {
                    cnt++;
                }
            }
            if (cnt > 2) {
                break;
            }
            min++;
        }
        System.out.println(min);
    }
}