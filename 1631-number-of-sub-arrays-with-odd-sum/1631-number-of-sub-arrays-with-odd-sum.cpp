#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int numOfSubarrays(vector<int>& arr) {
        const int MOD = 1e9 + 7;
        int evenCount = 1, oddCount = 0;  // evenCount starts at 1 (prefixSum = 0 is even)
        int prefixSum = 0, result = 0;

        for (int num : arr) {
            prefixSum += num;
            if (prefixSum % 2 == 0) { 
                result = (result + oddCount) % MOD;  // Only oddCount contributes
                evenCount++;  // Update even prefix count
            } else { 
                result = (result + evenCount) % MOD;  // Only evenCount contributes
                oddCount++;  // Update odd prefix count
            }
        }
        return result;
    }
};
