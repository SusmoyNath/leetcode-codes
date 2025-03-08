#include <vector>

class Solution {
public:
    void backtrack(int start, int k, int n, std::vector<int>& path, std::vector<std::vector<int>>& result) {
        if (k == 0 && n == 0) {
            result.push_back(path);
            return;
        }
        if (k == 0 || n < 0) return;

        for (int i = start; i <= 9; i++) {
            path.push_back(i);
            backtrack(i + 1, k - 1, n - i, path, result);
            path.pop_back();  // Backtrack
        }
    }

    std::vector<std::vector<int>> combinationSum3(int k, int n) {
        std::vector<std::vector<int>> result;
        std::vector<int> path;
        backtrack(1, k, n, path, result);
        return result;
    }
};
