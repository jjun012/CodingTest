import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st=new StringTokenizer(br.readLine());
         int x =Integer.parseInt(st.nextToken());
         StringBuilder sb = new StringBuilder();

         for(int i=0;i< x;i++){
             st = new StringTokenizer(br.readLine());
             int a= Integer.parseInt(st.nextToken());
             int b =Integer.parseInt(st.nextToken());
             sb.append(a+b+"\n");


         }
        System.out.println(sb);
    }
}