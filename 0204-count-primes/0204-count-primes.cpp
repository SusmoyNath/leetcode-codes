class Solution {
public:
    int countPrimes(int n) {
        if (n <= 2) return 0;  // No primes below 2
        
        vector<bool> isPrime(n, true);
        isPrime[0] = isPrime[1] = false; // 0 and 1 are not prime
        
        for (int i = 2; i * i < n; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j < n; j += i) {
                    isPrime[j] = false;  // Mark multiples as non-prime
                }
            }
        }
        
        return count(isPrime.begin(), isPrime.end(), true); // Count remaining primes
    }
};
