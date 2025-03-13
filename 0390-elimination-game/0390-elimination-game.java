class Solution {
    public int lastRemaining(int n) {
        int head = 1;
        int step = 1;
        boolean left = true; // Track direction
        
        while (n > 1) {
            // If moving left or if the count is odd, move head forward
            if (left || (n % 2 == 1)) {
                head += step;
            }
            
            // Reduce the number of elements by half
            n /= 2;
            // Double the step
            step *= 2;
            // Toggle direction
            left = !left;
        }
        
        return head;
    }
}
