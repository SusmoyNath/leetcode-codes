#include <unordered_set>
#include <vector>
using namespace std;

class Solution {
public:
    int distributeCandies(vector<int>& candyType) {
        unordered_set<int> uniqueCandies(candyType.begin(), candyType.end());
        int maxAllowed = candyType.size() / 2;
        return min((int)uniqueCandies.size(), maxAllowed);
    }
};
