class Solution {
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        // Step 1: Sort by height descending, if height is the same, sort by k ascending
        sort(people.begin(), people.end(), [](vector<int>& a, vector<int>& b) {
            return (a[0] > b[0]) || (a[0] == b[0] && a[1] < b[1]);
        });

        // Step 2: Insert each person at their k position
        vector<vector<int>> queue;
        for (auto& person : people) {
            queue.insert(queue.begin() + person[1], person);
        }

        return queue;
    }
};
