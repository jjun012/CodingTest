import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int x= Integer.parseInt(br.readLine());
        double max=0;
        double sum=0;
        StringTokenizer st= new StringTokenizer(br.readLine());
        double[] a =new double[x];
        for(int i=0;i<a.length;i++){
            a[i]=Double.parseDouble(st.nextToken());
            if(a[i]>max){
                max=a[i];
            }
        }
        for(int i=0;i<a.length;i++){
            a[i]= (a[i]/max)*100;
            sum += a[i];
        }

        System.out.println(sum/a.length);
    }
}