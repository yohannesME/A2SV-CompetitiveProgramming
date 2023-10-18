class Solution {
public:
    int largestOverlap(vector<vector<int>>& img1, vector<vector<int>>& img2) {
        int N = img1.size();
        int ans = 0;
        for(int dx = -N; dx < N; dx++ ){
            for(int dy = -N; dy < N; dy++){
                int count = 0;

                for(int x = 0; x < N; x++){
                    int nx = x + dx;
                    if(nx >= 0 && nx < N)
                        for(int y = 0; y < N; y++){
                            int ny = y + dy;

                            if(ny >= 0 && ny < N)
                            if(img1[x][y] == 1 && img2[nx][ny] == 1) count++;
                        }
                }
                ans = max(ans, count);
            }
        }

        return ans;
    }
};