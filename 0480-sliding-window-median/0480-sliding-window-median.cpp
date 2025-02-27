class Solution {
public:
    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        vector<double> result;
        multiset<int> low, high; // Low stores smaller half, High stores larger half
        
        for (int i = 0; i < nums.size(); i++) {
            // Insert new element into the appropriate heap
            if (low.empty() || nums[i] <= *low.rbegin()) 
                low.insert(nums[i]);
            else 
                high.insert(nums[i]);

            // Balance the two heaps
            while (low.size() > high.size() + 1) {
                high.insert(*low.rbegin());
                low.erase(prev(low.end()));
            }
            while (high.size() > low.size()) {
                low.insert(*high.begin());
                high.erase(high.begin());
            }

            // Remove the element that is sliding out of the window
            if (i >= k) {
                int toRemove = nums[i - k];
                if (low.count(toRemove)) 
                    low.erase(low.find(toRemove));
                else 
                    high.erase(high.find(toRemove));

                // Rebalance again after removal
                while (low.size() > high.size() + 1) {
                    high.insert(*low.rbegin());
                    low.erase(prev(low.end()));
                }
                while (high.size() > low.size()) {
                    low.insert(*high.begin());
                    high.erase(high.begin());
                }
            }

            // Push median to the result once the first k elements are processed
            if (i >= k - 1) {
                if (k % 2 == 1)
                    result.push_back((double) *low.rbegin());
                else
                    result.push_back(0.5 * ((long long) *low.rbegin() + (long long) *high.begin())); // Prevent overflow
            }
        }

        return result;
    }
};
