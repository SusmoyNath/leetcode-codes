#include <bits/stdc++.h>
using namespace std;
 
typedef long long ll;
 
class Solution {
private:
    string s;
    unordered_map<ll, ll> memo;
    
    ll encodeState(int pos, int tight, int started, int hasZero, int sum, ll prod) {
        ll key = pos;
        key = key * 3 + tight;
        key = key * 3 + started;
        key = key * 3 + hasZero;
        key = key * 101 + sum;
        key = key * 4000000001LL + prod;
        return key;
    }
    
    ll dp(int pos, int tight, int started, int hasZero, int sum, ll prod) {
        if(pos == s.size()) return (!started ? 0 : (hasZero || (prod % sum == 0)) ? 1 : 0);
        
        ll stateKey = encodeState(pos, tight, started, hasZero, sum, prod);
        if(memo.find(stateKey) != memo.end()) return memo[stateKey];
        
        ll ans = 0;
        int limit = (tight ? s[pos]-'0' : 9);
        for (int d = 0; d <= limit; d++) {
            int newTight = (tight && (d == limit)) ? 1 : 0;
            if(!started && d == 0) {
                ans += dp(pos+1, newTight, 0, 0, 0, 1);
            } else {
                int newHasZero = hasZero || (d == 0);
                ll newProd = (hasZero || d == 0) ? 0 : prod * d;
                ans += dp(pos+1, newTight, 1, newHasZero, sum + d, newProd);
            }
        }
        
        return memo[stateKey] = ans;
    }
    
    ll countBeautiful(ll X) {
        if(X < 1) return 0;
        s = to_string(X);
        memo.clear();
        return dp(0, 1, 0, 0, 0, 1);
    }
 
public:
    int beautifulNumbers(int l, int r) {
        return (int)(countBeautiful(r) - countBeautiful(l - 1));
    }
};
