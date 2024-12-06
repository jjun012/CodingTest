import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int x=Integer.parseInt(br.readLine());

        if(x>=90 && x<=100){
            System.out.println("A");
        }else if(x>=80){
            System.out.println("B");
        }else if(x>=70){
            System.out.println("C");
        } else if (x>=60) {
            System.out.println("D");
        }else{
            System.out.println("F");
        }
    }
}