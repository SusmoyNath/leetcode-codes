class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buy1 = INT_MIN, sell1 = 0, buy2 = INT_MIN, sell2 = 0;
        
        for (int price : prices) {
            buy1 = max(buy1, -price);         // First buy
            sell1 = max(sell1, buy1 + price); // First sell
            buy2 = max(buy2, sell1 - price);  // Second buy
            sell2 = max(sell2, buy2 + price); // Second sell
        }
        
        return sell2; // Maximum profit after two transactions
    }
};
