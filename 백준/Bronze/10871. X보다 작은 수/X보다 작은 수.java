import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());

        int x= Integer.parseInt(st.nextToken());
        int y= Integer.parseInt(st.nextToken());
        int []array= new int[x];
        st = new StringTokenizer(br.readLine()," ");
        for(int i=0;i< array.length;i++){
            array[i]=Integer.parseInt(st.nextToken());
        }
        for(int i=0;i< array.length;i++){
            if(array[i]<y) {
                System.out.print(array[i] + " ");
            }
        }
    }
}