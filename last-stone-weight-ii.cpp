class Solution {
public:
    int knapsack(int W, vector<int> &wt, int n){
        // build table k[][] in bottom up manner
        vector<vector<int>> K(n+1, vector<int>(W + 1));

        for(int i = 0; i <= n; i++){
            for(int w = 0; w <= W; w++){
                if(i == 0 || w == 0){
                    K[i][w] = 0;
                }else if(wt[i - 1] <= w){
                    K[i][w] = std::max(wt[i-1] + K[i-1][w - wt[i-1]], K[i-1][w]);
                }else{
                    K[i][w] = K[i-1][w];
                }
            }

        }

        return K[n][W];
    }

    int lastStoneWeightII(vector<int>& stones) {
        int totalsum = 0;

        for(int i = 0; i < stones.size(); i++){
            totalsum += stones[i];
        }

        int val = knapsack(totalsum/2, stones, stones.size());

        return abs(-totalsum + 2*val);
    }
};