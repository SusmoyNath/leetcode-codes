class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        if (points.empty()) return 0;
        
        // Sort balloons by their ending positions
        sort(points.begin(), points.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[1] < b[1]; // Sort by xend
        });

        int arrows = 1;
        int lastArrowPosition = points[0][1]; // Place first arrow at the end of the first balloon

        for (int i = 1; i < points.size(); i++) {
            if (points[i][0] > lastArrowPosition) {
                // If the balloon's start is beyond lastArrowPosition, we need a new arrow
                arrows++;
                lastArrowPosition = points[i][1]; // Place new arrow at the end of this balloon
            }
        }

        return arrows;
    }
};
