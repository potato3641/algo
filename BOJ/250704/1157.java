import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String target = sc.nextLine();
        target = target.toUpperCase();
        Map<Character, Integer> map = new HashMap<>();
        for (int i=0; i<target.length(); i++) {
            Character temp = target.charAt(i);
            if (map.containsKey(temp)) {
                map.put(temp, map.get(temp)+1);
            } else {
                map.put(temp, 1);
            }
        }
        int maxValue = Collections.max(map.values());
        List<Character> list = new ArrayList<>();
        for (Character key : map.keySet()) {
            if (map.get(key) == maxValue) {
                list.add(key);
            }
        }
        if (list.size() > 1) {
            System.out.println("?");
        } else {
            System.out.println(list.get(0));
        }
    }
}