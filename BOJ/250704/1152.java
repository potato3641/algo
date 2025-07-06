import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        String[] sep = line.split(" ");
        int cnt = 0;
        for (String e : sep) {
            if (e.length() > 0) {
                cnt++;
            }
        }
        System.out.println(cnt);
    }
}