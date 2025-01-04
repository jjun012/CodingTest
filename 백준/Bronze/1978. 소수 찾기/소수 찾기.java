import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        int N= Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] a = new int [N];
        int count =0;
        for(int i=0;i<N;i++){
            a[i]=Integer.parseInt(st.nextToken());

            for(int j=2;j<=a[i];j++){
                if(j==a[i]){
                    count++;}
                if(a[i]%j==0)
                    break;
            }
        }
        System.out.println(count);
    }
}