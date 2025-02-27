class Solution {
public:
    int largestPalindrome(int n) {
        if (n == 1) return 9;  // Special case: 1-digit numbers (max product = 9)
        
        int upper = pow(10, n) - 1; // Largest n-digit number
        int lower = pow(10, n-1);   // Smallest n-digit number
        
        for (long long left = upper; left >= lower; --left) {
            long long palindrome = buildPalindrome(left);
            
            // Try to factorize the palindrome
            for (long long i = upper; i * i >= palindrome; --i) {
                if (palindrome % i == 0) {
                    long long j = palindrome / i;
                    if (j >= lower && j <= upper) {
                        return palindrome % 1337;
                    }
                }
            }
        }
        
        return -1; // Should never reach here
    }
    
private:
    long long buildPalindrome(long long left) {
        string s = to_string(left);
        reverse(s.begin(), s.end());
        return stoll(to_string(left) + s); // Mirror left half
    }
};
