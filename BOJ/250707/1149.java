import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException{
        Scanner sc = new Scanner(System.in);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        List<List<Integer>> dp = new ArrayList<>();
        for (int i=0; i<N; i++) {
            dp.add(new ArrayList<>(Arrays.asList(0,0,0)));
        }
        for (int i=0; i<N; i++) {
            int[] rgb = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            if (i > 0) {
                dp.get(i).set(0, rgb[0]+Math.min(dp.get(i-1).get(1), dp.get(i-1).get(2)));
                dp.get(i).set(1, rgb[1]+Math.min(dp.get(i-1).get(2), dp.get(i-1).get(0)));
                dp.get(i).set(2, rgb[2]+Math.min(dp.get(i-1).get(0), dp.get(i-1).get(1)));
            } else {
                dp.get(i).set(0, rgb[0]);
                dp.get(i).set(1, rgb[1]);
                dp.get(i).set(2, rgb[2]);
            }
        }
        System.out.println(Collections.min(dp.get(N-1)));
    }
}