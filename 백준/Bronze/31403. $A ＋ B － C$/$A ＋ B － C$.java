import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int x = Integer.parseInt(br.readLine());
        int y= Integer.parseInt(br.readLine());
        int z= Integer.parseInt(br.readLine());
        String s="";
        s+=x;
        s+=y;
        System.out.println(x+y-z);
        System.out.println(Integer.parseInt(s)-z);
    }
}