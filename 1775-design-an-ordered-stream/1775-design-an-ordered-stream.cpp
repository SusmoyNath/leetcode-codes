class OrderedStream {
private:
    vector<string> stream;
    int ptr;

public:
    OrderedStream(int n) {
        stream.resize(n);
        ptr = 0;
    }
    
    vector<string> insert(int idKey, string value) {
        stream[idKey - 1] = value;  // Store value at index (idKey - 1)
        vector<string> result;

        // Start collecting values from ptr if they are non-empty
        while (ptr < stream.size() && !stream[ptr].empty()) {
            result.push_back(stream[ptr]);
            ptr++;  // Move pointer to the next expected position
        }

        return result;
    }
};

