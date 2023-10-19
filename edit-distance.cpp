class Solution {
public:
    int dp[505][505];
    int minDistance(string word1, string word2) {
        int n1 = word1.length();
        int n2 = word2.length();

        if(n1 == 0 || n2 == 0) return max(n1, n2);

        for(int i = 0; i <= n2; i++){
            for(int j = 0; j <= n1; j++){
                dp[i][j] = 5000;
            }
        }

        dp[0][0] = 0;

        for(int i = 0; i <= n2; i++){
            for(int j = 0; j <= n1; j++){
                if(word2[i] == word1[j]) {
                    dp[i+1][j+1] = min(dp[i][j], dp[i+1][j+1]);
                    continue;
                }
                dp[i+1][j] = min(dp[i][j] + 1, dp[i+1][j]);
                dp[i][j+1] = min(dp[i][j] + 1, dp[i][j+1]);
                dp[i+1][j+1] = min(dp[i][j] + 1, dp[i+1][j+1]);

            }
        }
        

        return dp[n2][n1];
    }
};