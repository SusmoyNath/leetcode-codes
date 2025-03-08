class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int> inDegree(numCourses, 0);
        vector<vector<int>> adj(numCourses);

        // Step 1: Build adjacency list & in-degree array
        for (auto& pre : prerequisites) {
            int course = pre[0];
            int prerequisite = pre[1];
            adj[prerequisite].push_back(course);
            inDegree[course]++;
        }

        // Step 2: Add courses with zero prerequisites to queue
        queue<int> q;
        for (int i = 0; i < numCourses; i++) {
            if (inDegree[i] == 0) q.push(i);
        }

        // Step 3: Process courses using BFS
        int processedCourses = 0;
        while (!q.empty()) {
            int course = q.front();
            q.pop();
            processedCourses++;

            for (int nextCourse : adj[course]) {
                if (--inDegree[nextCourse] == 0) {
                    q.push(nextCourse);
                }
            }
        }

        // Step 4: If all courses are processed, return true
        return processedCourses == numCourses;
    }
};
