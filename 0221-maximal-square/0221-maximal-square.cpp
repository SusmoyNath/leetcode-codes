#include <vector>
#include <algorithm>

class Solution {
public:
    int maximalSquare(std::vector<std::vector<char>>& matrix) {
        if (matrix.empty() || matrix[0].empty()) return 0;
        
        int m = matrix.size(), n = matrix[0].size();
        std::vector<int> prev(n + 1, 0), curr(n + 1, 0);
        int maxSize = 0;

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (matrix[i - 1][j - 1] == '1') {
                    curr[j] = std::min({prev[j], curr[j - 1], prev[j - 1]}) + 1;
                    maxSize = std::max(maxSize, curr[j]);
                } else {
                    curr[j] = 0;
                }
            }
            std::swap(prev, curr); // Move to next row
        }

        return maxSize * maxSize;
    }
};
