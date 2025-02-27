class Solution {
public:
    int getMaxRepetitions(string s1, int n1, string s2, int n2) {
        if (n1 == 0) return 0;

        int s1_len = s1.size(), s2_len = s2.size();
        int index = 0, count_s2 = 0;
        unordered_map<int, pair<int, int>> seen; // {index in s2: {count_s1, count_s2}}

        for (int count_s1 = 0; count_s1 < n1; count_s1++) {
            for (char c : s1) {
                if (c == s2[index]) {
                    index++;
                    if (index == s2_len) {
                        count_s2++;
                        index = 0;
                    }
                }
            }
            
            if (seen.find(index) != seen.end()) {
                // Cycle detected
                auto [prev_s1, prev_s2] = seen[index];
                int cycle_s1 = count_s1 - prev_s1;
                int cycle_s2 = count_s2 - prev_s2;

                int remaining_s1 = (n1 - count_s1 - 1) / cycle_s1;
                count_s2 += remaining_s1 * cycle_s2;
                count_s1 += remaining_s1 * cycle_s1;
            }

            seen[index] = {count_s1, count_s2};
        }

        return count_s2 / n2;
    }
};
