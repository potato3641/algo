import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException{
        Scanner sc = new Scanner(System.in);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int switchN = Integer.parseInt(br.readLine());
        List<Integer> switchList = new ArrayList<>();
        switchList.add(0);
        Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).forEach(switchList::add);
        int studentN = Integer.parseInt(br.readLine());
        for (int i=0; i<studentN; i++) {
            int[] gen_num = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            int gen = gen_num[0];
            int num = gen_num[1];
            if (gen-1 > 0) {
                int cnt = 1;
                switchList.set(num, switchList.get(num)^1);
                while (true) {
                    if ((num + cnt) > switchN || (num-cnt) < 1) {
                        break;
                    }
                    if (switchList.get(num+cnt) == switchList.get(num-cnt)) {
                        switchList.set(num+cnt, switchList.get(num+cnt)^1);
                        switchList.set(num-cnt, switchList.get(num-cnt)^1);
                    } else {
                        break;
                    }
                    cnt += 1;
                }
            } else {
                for (int j=num;j<switchN+1;j += num) {
                    switchList.set(j, switchList.get(j)^1);
                }
            }
        }
        List<Integer> newList = new ArrayList<>(switchList.subList(1, switchList.size()));
        int i = 0;
        while (i < newList.size()) {
            int end = Math.min(i + 20, newList.size());
            List<Integer> printLine = newList.subList(i, end);
            stringPrinter(printLine);
            i += 20;
        }
    }
    public static <T> void stringPrinter(List<T> list) {
        StringJoiner joiner = new StringJoiner(" ");
        for (T n : list) {
            joiner.add(n.toString());
        }
        System.out.println(joiner.toString());
    }
}