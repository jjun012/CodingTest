import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int x=Integer.parseInt(br.readLine());

        for(int i=0;i<9;i++){
            System.out.println(x+" * "+(i+1)+" = "+(x*(i+1)));
        }
    }
}