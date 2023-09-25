#define lli long long int
#define ll long long

class Solution {
public:
    int longestPalindromeSubseq(string s) {
        int n = s.length();
        lli dp[n+1][n+1];

        for(int i = 0; i <= n; i++){
            for(int j = 0; j <= n; j++){
                dp[i][j] = 0;
            }
        }

        for(int i = n-1; i > -1; i--){
            for(int j = n-1; j > -1; j--){

                if (s[i] == s[n-1-j])
                    dp[i][j] = 1 + dp[i+1][j+1];
                else
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1]);
            }   
        }

        return dp[0][0];
    }
};