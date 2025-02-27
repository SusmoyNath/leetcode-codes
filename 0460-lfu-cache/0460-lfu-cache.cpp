#include <unordered_map>
#include <map>
#include <list>

using namespace std;

class LFUCache {
public:
    int capacity, minFreq;
    unordered_map<int, pair<int, int>> keyToValFreq;  // key -> {value, frequency}
    unordered_map<int, list<int>> freqToKeys;         // frequency -> list of keys
    unordered_map<int, list<int>::iterator> keyToIter;// key -> iterator to list node
    
    LFUCache(int capacity) {
        this->capacity = capacity;
        minFreq = 0;
    }

    int get(int key) {
        if (keyToValFreq.find(key) == keyToValFreq.end()) 
            return -1; // Key not found
        
        // Update frequency
        updateFrequency(key);
        return keyToValFreq[key].first;
    }

    void put(int key, int value) {
        if (capacity == 0) return; // Edge case: no capacity
        
        if (keyToValFreq.find(key) != keyToValFreq.end()) {
            keyToValFreq[key].first = value;
            updateFrequency(key);
            return;
        }
        
        // Cache is full -> Remove LFU item
        if (keyToValFreq.size() >= capacity) {
            int evictKey = freqToKeys[minFreq].back();
            freqToKeys[minFreq].pop_back();
            keyToValFreq.erase(evictKey);
            keyToIter.erase(evictKey);
            if (freqToKeys[minFreq].empty()) freqToKeys.erase(minFreq);
        }

        // Insert new key with freq = 1
        minFreq = 1;
        keyToValFreq[key] = {value, 1};
        freqToKeys[1].push_front(key);
        keyToIter[key] = freqToKeys[1].begin();
    }

private:
    void updateFrequency(int key) {
        int freq = keyToValFreq[key].second;
        keyToValFreq[key].second++; // Increase frequency

        // Remove from old frequency list
        freqToKeys[freq].erase(keyToIter[key]);
        if (freqToKeys[freq].empty()) {
            freqToKeys.erase(freq);
            if (minFreq == freq) minFreq++;
        }

        // Add to new frequency list
        freqToKeys[freq + 1].push_front(key);
        keyToIter[key] = freqToKeys[freq + 1].begin();
    }
};
