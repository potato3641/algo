import java.util.*;
import java.io.*;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String lineA = br.readLine();
        String lineB = br.readLine();
        List<Integer> NofA = Arrays.stream(lineA.split(" ")).map(Integer::parseInt).collect(Collectors.toList());
        List<Integer> NofB = Arrays.stream(lineB.split(" ")).map(Integer::parseInt).collect(Collectors.toList());
        Collections.sort(NofA, Comparator.reverseOrder());
        Collections.sort(NofB);
        int answer = 0;
        for (int i=0; i<N; i++) {
            int a = NofA.get(i);
            int b = NofB.get(i);
            answer += a*b;
        }
        System.out.println(answer);
    }
}