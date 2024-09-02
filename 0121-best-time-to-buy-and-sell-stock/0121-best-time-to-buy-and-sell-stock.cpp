class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minimum = INT_MAX;
        int maximum = 0;
    
        for (int i = 0; i < prices.size(); i++) {
        if (prices[i] < minimum) {
            minimum = prices[i];
        } else if (prices[i] - minimum > maximum) {
            maximum = prices[i] - minimum;
        }
        }
    
        return maximum;
    
    }
};