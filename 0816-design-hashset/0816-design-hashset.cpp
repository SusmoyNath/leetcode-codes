#include <vector>
#include <list>

class MyHashSet {
private:
    static const int SIZE = 10000; // Size of the hash table
    std::vector<std::list<int>> table; // Array of lists for chaining
    
    int hash(int key) {
        return key % SIZE; // Simple modulo hash function
    }
    
public:
    MyHashSet() : table(SIZE) {}
    
    void add(int key) {
        int index = hash(key);
        for (int val : table[index]) {
            if (val == key) return; // Key already exists
        }
        table[index].push_back(key);
    }
    
    void remove(int key) {
        int index = hash(key);
        table[index].remove(key); // Removes key if it exists
    }
    
    bool contains(int key) {
        int index = hash(key);
        for (int val : table[index]) {
            if (val == key) return true;
        }
        return false;
    }
};