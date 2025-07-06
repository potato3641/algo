import java.util.*;

public class Main {
    public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int F = sc.nextInt();
		N = (N/100)*100;
		int target = N%F;
		if (target == F) {
			System.out.println("00");
		} else {
			if (target > 0) {
				target = F-target;
			}
			System.out.println(String.format("%02d", target));
		}
	}
}