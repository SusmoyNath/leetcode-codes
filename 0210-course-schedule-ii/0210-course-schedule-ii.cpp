class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> adj(numCourses);  // Adjacency list
        vector<int> inDegree(numCourses, 0);  // In-degree array
        vector<int> order;  // Stores the course order
        
        // Build graph
        for (auto& pre : prerequisites) {
            int course = pre[0], prerequisite = pre[1];
            adj[prerequisite].push_back(course);
            inDegree[course]++;
        }
        
        // Queue for BFS
        queue<int> q;
        
        // Add courses with no prerequisites (in-degree == 0)
        for (int i = 0; i < numCourses; i++) {
            if (inDegree[i] == 0) q.push(i);
        }
        
        // Process queue
        while (!q.empty()) {
            int course = q.front();
            q.pop();
            order.push_back(course);
            
            // Reduce in-degree of dependent courses
            for (int next : adj[course]) {
                inDegree[next]--;
                if (inDegree[next] == 0) q.push(next);
            }
        }
        
        // If we processed all courses, return order; otherwise, return empty list (cycle detected)
        return (order.size() == numCourses) ? order : vector<int>();
    }
};
