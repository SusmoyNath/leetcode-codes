class Solution {
public:
    int numberOfAlternatingGroups(vector<int>& colors, int k) {
        int n = colors.size();
        int count = 0, valid = 1; // Valid flag (1 if alternating, 0 otherwise)

        // Check if the first `k` elements form an alternating group
        for (int i = 0; i < k - 1; i++) {
            if (colors[i] == colors[i + 1]) {
                valid = 0;
                break;
            }
        }
        count += valid; // If the first k-group is valid, increment count

        // Sliding window across the circular array
        for (int i = 1; i < n; i++) {
            int prev_start = (i - 1) % n;
            int new_end = (i + k - 1) % n;

            // If the outgoing element disrupted the alternation, reset valid
            if (colors[prev_start] == colors[(prev_start + 1) % n]) {
                valid = 1;
                for (int j = 0; j < k - 1; j++) {
                    if (colors[(i + j) % n] == colors[(i + j + 1) % n]) {
                        valid = 0;
                        break;
                    }
                }
            }
            // If the new incoming element disrupts the alternation, mark invalid
            else if (colors[new_end] == colors[(new_end - 1 + n) % n]) {
                valid = 0;
            }

            count += valid; // Only count if valid remains 1
        }

        return count;
    }
};
