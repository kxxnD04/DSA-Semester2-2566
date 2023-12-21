import java.util.*;
public class Test {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        MyAdd cm = new MyAdd();
        System.out.println("Please insert number : ");
        int x = scn.nextInt();
        int num = cm.AddTwo(x);
        System.out.println(num);
        
        num = cm.AddTwo(x+5);
        System.out.println(num);
        
        num = cm.AddTwo(x*3+2);
        System.out.println(num);
    }
}
