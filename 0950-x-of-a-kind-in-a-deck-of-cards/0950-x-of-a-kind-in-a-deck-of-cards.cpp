#include <vector>
#include <unordered_map>
#include <numeric>

using namespace std;

class Solution {
public:
    bool hasGroupsSizeX(vector<int>& deck) {
        if (deck.size() < 2) return false;

        unordered_map<int, int> freq;
        for (int card : deck) {
            freq[card]++;
        }

        int gcdValue = 0;
        for (auto& [_, count] : freq) {
            gcdValue = gcd(gcdValue, count);
        }

        return gcdValue >= 2;
    }
};
