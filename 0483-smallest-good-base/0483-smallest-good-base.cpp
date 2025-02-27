#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string smallestGoodBase(string n) {
        long long N = stoll(n);  // Convert string to long long
        
        // Try different lengths (m+1) from log2(N) down to 2
        for (int m = log2(N); m >= 1; --m) {
            long long left = 2, right = pow(N, 1.0 / m);  // Limit the search space

            while (left <= right) {
                long long k = left + (right - left) / 2;
                long long sum = 1, term = 1;

                // Compute geometric sum
                for (int i = 1; i <= m; ++i) {
                    if (sum > N / k) {  // Prevent overflow
                        sum = N + 1;
                        break;
                    }
                    term *= k;
                    sum += term;
                }

                if (sum == N) return to_string(k);
                if (sum < N) left = k + 1;
                else right = k - 1;
            }
        }

        // If no valid base is found, return N-1 as the default base
        return to_string(N - 1);
    }
};
