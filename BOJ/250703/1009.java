import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		List<Integer> same = Arrays.asList(0, 1, 5, 6);
		Map<Integer, List<Integer>> map = new HashMap<>();
		map.put(2, Arrays.asList(2,4,8,6));
		map.put(3,Arrays.asList(3,9,7,1));
		map.put(4,Arrays.asList(4,6));
		map.put(7,Arrays.asList(7,9,3,1));
		map.put(8,Arrays.asList(8,4,2,6));
		map.put(9, Arrays.asList(9,1));
		int N = sc.nextInt();
		for (int i = 0; i < N; i++) {
			int A = sc.nextInt();
			int B = sc.nextInt();
			A %= 10;
			if (same.contains(A)) {
				System.out.println(A > 0 ? A : 10);
			} else {
				int size = map.get(A).size();
				B -= 1;
				B %= size;
				System.out.println(map.get(A).get(B));
			}
		}
	}
}