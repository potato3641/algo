import java.util.*;
public class Main {
    public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		Map<Integer, Integer> map = new HashMap<>();
		for (int i=0;i<N;i++) {
			int val = sc.nextInt();
			map.put(i, val);
		}
		Optional<Integer> minValOpt = map.values().stream().min(Comparator.naturalOrder());
		Optional<Integer> maxValOpt = map.values().stream().max(Comparator.naturalOrder());
		int minVal = minValOpt.get();
		int maxVal = maxValOpt.get();
		System.out.println(minVal*maxVal);
	}
}