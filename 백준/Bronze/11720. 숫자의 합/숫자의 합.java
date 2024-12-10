import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int x = Integer.parseInt(br.readLine());
        String[] array = br.readLine().split("");
        int sum = 0;
        br.close();
        for (int i = 0; i < x; i++) {
            sum += Integer.parseInt(array[i]);
        }
        System.out.println(sum);
    }
}