#include <vector>
#include <list>

class MyHashMap {
private:
    static const int SIZE = 10000; // Hash table size
    std::vector<std::list<std::pair<int, int>>> table; // Array of lists for chaining
    
    int hash(int key) {
        return key % SIZE; // Simple hash function
    }
    
public:
    MyHashMap() : table(SIZE) {}
    
    void put(int key, int value) {
        int index = hash(key);
        for (auto& pair : table[index]) {
            if (pair.first == key) {
                pair.second = value; // Update existing key
                return;
            }
        }
        table[index].emplace_back(key, value); // Insert new key-value pair
    }
    
    int get(int key) {
        int index = hash(key);
        for (const auto& pair : table[index]) {
            if (pair.first == key) return pair.second;
        }
        return -1; // Key not found
    }
    
    void remove(int key) {
        int index = hash(key);
        table[index].remove_if([key](const std::pair<int, int>& pair) { return pair.first == key; });
    }
};