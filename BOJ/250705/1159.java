import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        sc.nextLine();
        String giveUp = "PREDAJA";
        Map<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < N; i ++) {
            String name = sc.nextLine();
            Character first = name.charAt(0);
            if (map.containsKey(first)) {
                map.put(first, map.get(first)+1);
            } else {
                map.put(first, 1);
            }
        }
        List<String> list = new ArrayList<>();
        for (Character key : map.keySet()) {
            if (map.get(key) >= 5) {
                list.add(key.toString());
            }
        }
        Collections.sort(list);
        if (list.size() > 0) {
            System.out.println(String.join("", list));
        } else {
            System.out.println(giveUp);
        }
    }
}