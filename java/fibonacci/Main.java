import java.util.Scanner; 
import java.util.Arrays;

public class Main {
  public static int getFibonacci(int number) {
    if (number == 0) {
      return 0;
    } else if (number == 1) {
      return 1;
    } else {
      int a = getFibonacci(number - 2);
      int b = getFibonacci(number - 1);
      return a + b;
    }
  }

  public static int[] getByRecursion(int position) {
    int[] sequence;
    sequence = new int[position];

    for (int i = 0; i < position; i++) {
      sequence[i] = getFibonacci(i);
    }

    return sequence;
  }

  public static int[] getByLineal(int position) {
    int[] sequence;
    int new_v;
    sequence = new int[position];

    int less2 = 0;
    int less1 = 1;
 
    sequence[0] = less2;
    sequence[1] = less1;
    for (int i = 2; i < position; i++) {
      new_v = less2 + less1;
      sequence[i] = new_v;

      less2 = less1;
      less1 = new_v;
    }
    
    return sequence;
  }

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.print("Type Fibonacci Length: ");
    int position = sc.nextInt();
    
    if (position > 15) {
      int[] list = getByLineal(position);
      System.out.println("\n " + Arrays.toString(list));
      System.out.println("\nLineal mode implement");
    } else {
      int[] list = getByRecursion(position);
      System.out.println("\n " + Arrays.toString(list));
      System.out.println("\nRecursion mode implement");
    }
  }
}
