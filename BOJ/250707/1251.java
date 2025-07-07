import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException{
        Scanner sc = new Scanner(System.in);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String target = br.readLine();
        List<String> answer = new ArrayList<>();
        for (int i=1; i<target.length()-1; i++) {
            for (int j=i+1; j<target.length(); j++) {
                StringBuffer firstsb = new StringBuffer(target.substring(0, i));
                String first = firstsb.reverse().toString();
                StringBuffer secondsb = new StringBuffer(target.substring(i, j));
                String second = secondsb.reverse().toString();
                StringBuffer thirdsb = new StringBuffer(target.substring(j));
                String third = thirdsb.reverse().toString();
                answer.add(first+second+third);
            }
        }
        Collections.sort(answer);
        System.out.println(answer.get(0));
    }
    public static void stringPrinter(List<Long> list) {
        StringJoiner joiner = new StringJoiner(" ");
        for (Object n : list) {
            joiner.add(n.toString());
        }
        System.out.println(joiner.toString());
    }
}