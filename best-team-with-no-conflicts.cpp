class Solution {
public:

    // int dp(vector<vector<int>> &combined, map<int, map<int, int>>& memo ,int i = 0, int maxscore = 0){
    //     if(i >= combined.size()){
    //         return 0;
    //     }

    //     if(memo[i][maxscore]){
    //         return memo[i][maxscore];
    //     }

    //     if(combined[i][1] < maxscore){
    //         memo[i][maxscore] = dp(combined, memo, i+1, maxscore);
    //         return memo[i][maxscore];
    //     }

    //     memo[i][maxscore] =  max(combined[i][1] + dp(combined, memo, i+1, std::max(combined[i][1], maxscore)), dp(combined, memo, i+1, maxscore));

    //    return memo[i][maxscore];

    // }

    int bestTeamScore(vector<int>& scores, vector<int>& ages) {
        int n = scores.size();
        vector<vector<int>> combined;

        for(int i = 0; i < n; i++){
            combined.push_back(vector<int>());
            combined[i].push_back(ages[i]);
            combined[i].push_back(scores[i]);
        }
        sort(combined.begin(), combined.end());
        
        int dp[scores.size()];

        for(int i = 0; i < scores.size(); i++){
            dp[i] = combined[i][1];
        }


        for(int i = scores.size()-1; i >= 0; i--){
            for(int j = i+1; j < scores.size(); j++){
                if(combined[i][1] > combined[j][1])
                    continue;
                
                dp[i] = std::max(dp[i], combined[i][1] + dp[j]);    
            }
        }

        int maxval = 0;
        for(int i = 0; i < scores.size(); i++){
            maxval = std::max(maxval, dp[i]);
        }
        return maxval;
    }
};