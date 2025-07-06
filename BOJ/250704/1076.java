import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		List<String> color = Arrays.asList("black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white");
		int A = color.indexOf(sc.nextLine());
		int B = color.indexOf(sc.nextLine());
		int C = color.indexOf(sc.nextLine());
		System.out.println((A*10+B)*(long)Math.pow(10,C));
	}
}