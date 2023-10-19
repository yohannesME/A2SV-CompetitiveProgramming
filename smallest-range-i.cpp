class Solution {
public:
    int smallestRangeI(vector<int>& nums, int k) {
        int maxval = 0;
        int minval = 100000;

        for(auto num: nums){
            maxval = max(maxval, num);
            minval = min(minval, num);
        }

        // int mid = minval + ceil((maxval - minval)/2.0);

        // for(int i = 0; i < nums.size(); i++){
        //     if(nums[i] > mid) nums[i] += max(mid - nums[i], -k);
        //     else nums[i] += min(mid - nums[i], k);
        // }

        // maxval = 0;
        // minval = 100000;

        // for(auto num: nums){
        //     maxval = max(maxval, num);
        //     minval = min(minval, num);
        // }

        return max(0, (maxval- k) - (minval + k));
    }
};