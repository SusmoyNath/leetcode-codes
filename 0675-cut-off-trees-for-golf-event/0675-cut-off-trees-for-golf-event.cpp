#include <vector>
#include <queue>
#include <algorithm>
#include <unordered_set>

using namespace std;

class Solution {
public:
    int cutOffTree(vector<vector<int>>& forest) {
        int m = forest.size(), n = forest[0].size();
        vector<pair<int, int>> trees;
        
        // Step 1: Extract all trees and sort by height
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (forest[i][j] > 1)
                    trees.push_back({forest[i][j], i * n + j}); // Store as (height, index)
            }
        }
        sort(trees.begin(), trees.end()); // Sort by height
        
        // Directions for movement (Up, Down, Left, Right)
        int dir[4][2] = {{-1,0}, {1,0}, {0,-1}, {0,1}};
        
        auto bfs = [&](int sr, int sc, int tr, int tc) -> int {
            if (sr == tr && sc == tc) return 0; // Already at target
            
            queue<pair<int, int>> q;
            q.push({sr, sc});
            vector<vector<int>> dist(m, vector<int>(n, -1));
            dist[sr][sc] = 0;

            while (!q.empty()) {
                auto [r, c] = q.front();
                q.pop();
                for (auto [dr, dc] : dir) {
                    int nr = r + dr, nc = c + dc;
                    if (nr >= 0 && nr < m && nc >= 0 && nc < n && forest[nr][nc] > 0 && dist[nr][nc] == -1) {
                        dist[nr][nc] = dist[r][c] + 1;
                        if (nr == tr && nc == tc) return dist[nr][nc]; // Found target
                        q.push({nr, nc});
                    }
                }
            }
            return -1; // Target unreachable
        };

        // Step 2: Traverse trees in order and calculate the shortest paths
        int totalSteps = 0;
        int sr = 0, sc = 0;

        for (auto [_, index] : trees) {
            int tr = index / n, tc = index % n;
            int steps = bfs(sr, sc, tr, tc);
            if (steps == -1) return -1; // If any tree is unreachable
            totalSteps += steps;
            sr = tr, sc = tc; // Move to next tree's position
        }
        
        return totalSteps;
    }
};
