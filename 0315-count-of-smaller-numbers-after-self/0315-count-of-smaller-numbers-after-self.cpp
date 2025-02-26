#include <vector>
#include <algorithm>
#include <unordered_map>
using namespace std;

class FenwickTree {
public:
    vector<int> tree;
    int size;
    
    FenwickTree(int n) {
        size = n;
        tree.resize(n + 1, 0);
    }

    void update(int index, int delta) {
        while (index <= size) {
            tree[index] += delta;
            index += index & -index;
        }
    }

    int query(int index) {
        int sum = 0;
        while (index > 0) {
            sum += tree[index];
            index -= index & -index;
        }
        return sum;
    }
};

class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        vector<int> sorted_nums(nums.begin(), nums.end());
        sort(sorted_nums.begin(), sorted_nums.end());
        
        // Coordinate Compression
        unordered_map<int, int> rank;
        for (int i = 0; i < sorted_nums.size(); i++) {
            rank[sorted_nums[i]] = i + 1;
        }

        // BIT for counting occurrences
        FenwickTree BIT(sorted_nums.size());
        vector<int> res(nums.size());

        // Process elements from right to left
        for (int i = nums.size() - 1; i >= 0; --i) {
            int r = rank[nums[i]];
            res[i] = BIT.query(r - 1);
            BIT.update(r, 1);
        }

        return res;
    }
};
