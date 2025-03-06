#include <queue>
#include <vector>

class KthLargest {
private:
    std::priority_queue<int, std::vector<int>, std::greater<int>> minHeap; // Min-heap to store k largest elements
    int k; // Store the value of k

public:
    KthLargest(int k, std::vector<int>& nums) {
        this->k = k;
        for (int num : nums) {
            add(num); // Insert elements while maintaining heap of size k
        }
    }
    
    int add(int val) {
        minHeap.push(val); // Add new element to the heap
        if (minHeap.size() > k) {
            minHeap.pop(); // Remove smallest element if heap size exceeds k
        }
        return minHeap.top(); // The top element is the kth largest
    }
};
