class Solution {
public:
    bool isPrime(int n) {
        if (n < 2) return false;
        if (n == 2) return true;
        if (n % 2 == 0) return false;
        for (int i = 3; i * i <= n; i += 2) {
            if (n % i == 0) return false;
        }
        return true;
    }

    int countPrimeSetBits(int left, int right) {
        int count = 0;
        for (int num = left; num <= right; ++num) {
            int setBits = __builtin_popcount(num); // Count set bits in binary representation
            if (isPrime(setBits)) {
                count++;
            }
        }
        return count;
    }
};
