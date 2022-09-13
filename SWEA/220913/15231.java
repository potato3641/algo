import java.util.Scanner;
import java.io.FileInputStream;
class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();
		for(int test_case = 1; test_case <= T; test_case++)
		{
            String var1 = sc.next();
            String var2 = sc.next();
            int N = 0;
            int V = 0;
            int rst;
            double underlog = Math.log(2.0);
            //System.out.println(Math.floor(Math.log(Double.parseDouble(var1))/underlog));
            N = (int) Math.floor(Math.log(Double.parseDouble(var1))/underlog);
            V = (int) Math.floor(Math.log(Double.parseDouble(var2))/underlog);
            rst = N+V;
            if ( ( Integer.parseInt(var1) < Math.floor((Math.pow(2,N) + Math.pow(2,N+1))/2) ) & ( Integer.parseInt(var2) < Math.floor((Math.pow(2,V) + Math.pow(2,V+1))/2) ) ) {
                
                rst -= 1;
            }
            System.out.print("#");
            System.out.print(test_case);
            System.out.print(" ");
            System.out.println(rst);
		}
	}
}
