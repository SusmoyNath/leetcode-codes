class Solution {
    public int fib(int n) {
        if (n == 0) return 0;
        if (n == 1) return 1;

        int[][] F = {{1, 1}, {1, 0}};
        power(F, n - 1);
        return F[0][0]; // The result is stored at F[0][0]
    }

    private void power(int[][] F, int n) {
        if (n == 0 || n == 1) return;

        int[][] M = {{1, 1}, {1, 0}};

        power(F, n / 2);
        multiply(F, F); // Square the matrix

        if (n % 2 != 0) multiply(F, M); // If n is odd, multiply by the base matrix
    }

    private void multiply(int[][] F, int[][] M) {
        int x = F[0][0] * M[0][0] + F[0][1] * M[1][0];
        int y = F[0][0] * M[0][1] + F[0][1] * M[1][1];
        int z = F[1][0] * M[0][0] + F[1][1] * M[1][0];
        int w = F[1][0] * M[0][1] + F[1][1] * M[1][1];

        F[0][0] = x;
        F[0][1] = y;
        F[1][0] = z;
        F[1][1] = w;
    }
}

// â Main method for testing
public class Fibonacci {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int n = 50; // Change this to test different values of n
        System.out.println("Fibonacci(" + n + ") = " + solution.fib(n));
    }
}
