class Solution {
public:
    int findNthDigit(int n) {
        long long digitLength = 1; // 1-digit, 2-digit, 3-digit, ...
        long long count = 9;       // Number of integers in each group (9, 90, 900, ...)
        long long start = 1;       // Starting number of each group (1, 10, 100, ...)

        // Step 1: Find the range where the nth digit belongs
        while (n > digitLength * count) {
            n -= digitLength * count; // Move to next range
            digitLength++;             // Increase digit length
            count *= 10;               // Increase count of numbers
            start *= 10;               // Move to next starting number
        }

        // Step 2: Find the exact number
        long long number = start + (n - 1) / digitLength; // Compute the exact number
        
        // Step 3: Find the exact digit in the number
        string numStr = to_string(number);
        return numStr[(n - 1) % digitLength] - '0'; // Convert character to integer
    }
};
