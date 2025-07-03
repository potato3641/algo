import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		sc.nextLine();
		Map<Integer, String> map = new HashMap<>();
		for (int i=0;i<N;i++) {
			String line = sc.nextLine();
			map.put(i, line);
		}
		
		int size = map.get(0).length();
		String sample = map.get(0);
		StringJoiner joiner = new StringJoiner("");
		for (int i=0; i<size;i++) {
			Set<Character> temp = new HashSet<>();
			for (int j=0;j<N;j++) {
				temp.add(map.get(j).charAt(i));
			}
			if (temp.size() > 1) {
				joiner.add("?");
			} else {
				char myc = sample.charAt(i);
				joiner.add(String.valueOf(myc));
			}
		}
		System.out.println(joiner.toString());
	}
}