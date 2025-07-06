import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int varN = sc.nextInt();
        int varm = sc.nextInt();
        int varM = sc.nextInt();
        int varT = sc.nextInt();
        int varR = sc.nextInt();
        int timer = 0;
        int heart = varm;
        if (varm+varT <= varM) {
            while (varN > 0) {
                if (heart+varT<= varM) {
                    heart += varT;
                    varN--;
                } else {
                    if (heart-varR < varm) {
                        heart = varm;
                    } else {
                        heart -= varR;
                    }
                }
                timer++;
            }
        } else {
            timer = -1;
        }
        System.out.println(timer);
    }
}