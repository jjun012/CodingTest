import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        int x= Integer.parseInt(br.readLine());

        int[] a= new int[6];
        StringTokenizer a1= new StringTokenizer(br.readLine());
        for( int i=0;i<6;i++){
            a[i]= Integer.parseInt(a1.nextToken());
        }

        StringTokenizer b1= new StringTokenizer(br.readLine());
        int[] b= new int[2];
        int sum=0;
        for(int i=0;i<2;i++){
            b[i]=Integer.parseInt(b1.nextToken());
        }
        for(int i=0;i<6;i++){
            if(a[i]%b[0]==0){
                a[i]=a[i]/b[0];
            }else {
                a[i] = a[i] / b[0] + 1;
            }
            sum+=a[i];
        }
        System.out.println(sum);
        int pen1= x/b[1];
        int pen2= x%b[1];
        System.out.println(pen1+" "+pen2);
    }
}