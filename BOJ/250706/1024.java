import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        String[] arr = line.split(" ");
        long N = Long.parseLong(arr[0]);
        int L = Integer.parseInt(arr[1]);
        stringPrinter(spliter(N, L));
    }
    public static List<Long> spliter(long N, int L) {
        if (L == 2 && N % 2 == 0) { // 짝수, 2
            return spliter(N, L+1);
        } else if (L == 2 && N % 2 == 1) { // 홀수, 2
            long even_pivot1 = N/2;
            long even_pivot2 = N/2+1;
            return Arrays.asList(even_pivot1, even_pivot2);
        } else if (L <= 100 && L%2 == 1 && N%L == 0) { // 피제수, 홀수
            long odd_pivot = N/L;
            long even_pivot1 = odd_pivot-1;
            long even_pivot2 = odd_pivot+1;
            int volume = L-3;
            List<Long> list = new ArrayList<>(Arrays.asList(odd_pivot, even_pivot1, even_pivot2));
            while (volume > 0) {
                even_pivot1 -= 1;
                even_pivot2 += 1;
                list.add(even_pivot1);
                list.add(even_pivot2);
                volume -= 2;
            }
            if (Collections.min(list) < 0) {
                return spliter(N, L+1);
            } else {
                Collections.sort(list);
                return list;
            }
        } else if (L <= 100 && L%2 == 0 && N%(L/2) == 0) {  // L/2피제수, 짝수
            long odd_pivot = N/(L/2);
            if (odd_pivot%2==1) {
                long even_pivot1 = odd_pivot/2;
                long even_pivot2 = odd_pivot/2+1;
                int volume = L-2;
                List<Long> list = new ArrayList<>(Arrays.asList(even_pivot1, even_pivot2));
                while (volume > 0) {
                    even_pivot1 -= 1;
                    even_pivot2 += 1;
                    list.add(even_pivot1);
                    list.add(even_pivot2);
                    volume -= 2;
                }
                if (Collections.min(list) < 0) {
                    return spliter(N, L+1);
                } else {
                    Collections.sort(list);
                    return list;
                }
            } else {
                return spliter(N, L+1);
            }
        } else if (L <= 100) { 
            return spliter(N, L+1);
        } else {
            return Arrays.asList(-1L);
        }
    }
    public static void stringPrinter(List<Long> list) {
        StringJoiner joiner = new StringJoiner(" ");
        for (Object n : list) {
            joiner.add(n.toString());
        }
        System.out.println(joiner.toString());
    }
}