class Solution {
public:
    int guessNumber(int n) {
        long left = 1, right = n;
        
        while (left <= right) {
            long mid = left + (right - left) / 2;
            int res = guess(mid); // Call the API
            
            if (res == 0) return mid;    // Correct guess
            else if (res == -1) right = mid - 1;  // Guess is too high
            else left = mid + 1;  // Guess is too low
        }
        
        return -1; // Should never reach here
    }
};