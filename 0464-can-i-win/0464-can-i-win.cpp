#include <unordered_map>

class Solution {
public:
    std::unordered_map<int, bool> memo; // Cache for memoization

    bool canIWin(int maxChoosableInteger, int desiredTotal) {
        int sum = (maxChoosableInteger * (maxChoosableInteger + 1)) / 2;
        if (sum < desiredTotal) return false;  // Impossible to win
        if (desiredTotal <= 0) return true;  // First player wins immediately

        return canWin(0, maxChoosableInteger, desiredTotal);
    }

    bool canWin(int state, int maxNum, int remainingTotal) {
        if (remainingTotal <= 0) return false; // If total already reached, current player loses
        if (memo.count(state)) return memo[state];

        // Try each available number
        for (int i = 0; i < maxNum; ++i) {
            int mask = (1 << i); // Represents picking number (i+1)
            if ((state & mask) == 0) {  // If this number hasn't been used
                if (!canWin(state | mask, maxNum, remainingTotal - (i + 1))) {
                    return memo[state] = true;  // If opponent loses, current player wins
                }
            }
        }
        return memo[state] = false;  // No move forces a win, so the player loses
    }
};
