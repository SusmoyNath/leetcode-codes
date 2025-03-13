class Solution {
public:
    int fourSumCount(vector<int>& nums1, vector<int>& nums2, vector<int>& nums3, vector<int>& nums4) {
        unordered_map<int, int> sumCount;
        int count = 0;

        // Store all sums of pairs from nums1 and nums2
        for (int a : nums1) {
            for (int b : nums2) {
                sumCount[a + b]++;
            }
        }

        // Find complements in nums3 and nums4
        for (int c : nums3) {
            for (int d : nums4) {
                count += sumCount[-(c + d)];
            }
        }

        return count;
    }
};
