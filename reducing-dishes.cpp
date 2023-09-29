class Solution {
public:
    int maxSatisfaction(vector<int>& satisfaction) {
        sort(satisfaction.begin(), satisfaction.end());
        int n = satisfaction.size();
        int dp[n+1][n+1];

        memset(dp, 0, sizeof dp);
        for(int i = 0; i < n; i ++)dp[i][0] = 0;

        for(int j = 1; j <= n; j++){
            for(int i = 1; i <= n; i++){
                dp[i][j] = satisfaction[i-1]*j + dp[i-1][j-1];
            }
        }

        int ans = 0;
        for(int i = 0; i <= n; i++)ans = max(ans, dp[n][i]);
        return ans;
    }
};