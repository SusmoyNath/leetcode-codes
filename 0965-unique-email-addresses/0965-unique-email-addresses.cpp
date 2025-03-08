#include <unordered_set>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    int numUniqueEmails(vector<string>& emails) {
        unordered_set<string> uniqueEmails;

        for (const string& email : emails) {
            string local, domain;
            bool plusSeen = false;
            
            int i = 0;
            while (email[i] != '@') {
                if (email[i] == '+') {
                    plusSeen = true; // Ignore everything after '+'
                }
                if (!plusSeen && email[i] != '.') {
                    local += email[i]; // Add valid characters to local name
                }
                i++;
            }

            domain = email.substr(i); // Extract domain (from '@' onward)
            uniqueEmails.insert(local + domain);
        }

        return uniqueEmails.size();
    }
};
