#include <queue>

class RecentCounter {
private:
    std::queue<int> requests;
    
public:
    RecentCounter() {
        // No initialization needed for the queue.
    }
    
    int ping(int t) {
        requests.push(t);
        
        // Remove outdated requests (outside the 3000ms window)
        while (!requests.empty() && requests.front() < t - 3000) {
            requests.pop();
        }
        
        return requests.size(); // Number of valid requests in the window
    }
};