class Solution {
public:

    int calculateMinimumHP(vector<vector<int>>& dungeon) {
        int m, n;
         m = dungeon.size();
         n = dungeon[0].size();
    
        int dp[m+1][n+1];

        for(int i = 0; i < m+1; i++){
            for(int j = 0; j < n+1; j++){
                dp[i][j] = -2000;
            }
        }

        dp[m-1][n] = 0; 
        dp[m][n-1] = 0; 

        for(int i = m-1; i >= 0; i--){
            for(int j = n - 1; j >= 0; j--){
                // cout << "max - " << dp[i+1][j] << " and " << dp[i][j+1] << endl; 
                dp[i][j] = max(dp[i+1][j], dp[i][j+1]) + dungeon[i][j];
                
                if(dp[i][j] > 0){
                    dp[i][j] = 0;
                }

                // for(int r = 0; r < m+1; r++){
                //     for(int c = 0; c < n+1; c++){
                //         cout << dp[r][c] << " ";
                //     }
                //     cout << endl;
                // }
                // cout << endl;

            }
        }

        return abs(dp[0][0]) + 1;

        
    }
};