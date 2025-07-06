import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        String target = N + "";
        int count = 0;
        while (true) {
            int basket = 0;
            if (target.length() < 2) {
                basket = Integer.parseInt(target);
            } else {
                for (int i = 0; i<target.length(); i++) {
                    basket += Integer.parseInt(String.valueOf(target.charAt(i)));
                }
            }
            String stringBasket = basket + "";
            String left = target.charAt(target.length()-1)+"";
            String right = stringBasket.charAt(stringBasket.length()-1)+"";
            int tempTarget = Integer.parseInt(left+right);
            target = tempTarget + "";
            count++;
            if (target.equals(N+"")) {
                break;
            }
        }
        System.out.println(count);
    }
}