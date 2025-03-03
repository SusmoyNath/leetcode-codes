#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    int calPoints(vector<string>& ops) {
        vector<int> stack;
        
        for (const string& op : ops) {
            if (op == "C") {
                if (!stack.empty()) stack.pop_back();
            } 
            else if (op == "D") {
                if (!stack.empty()) stack.push_back(2 * stack.back());
            } 
            else if (op == "+") {
                if (stack.size() >= 2) {
                    int last = stack.back();
                    int secondLast = stack[stack.size() - 2];
                    stack.push_back(last + secondLast);
                }
            } 
            else {
                stack.push_back(stoi(op)); // Convert string to integer and add to stack
            }
        }
        
        int sum = 0;
        for (int score : stack) {
            sum += score;
        }
        
        return sum;
    }
};
