#define ll double

class Solution {
public:
    double myPow(double x, int n) {
        ll tempn = n;
        n = abs(n);
        ll base = x;
        ll ans = 1;
         while (n > 0){
             if(n & 1) ans *= base;
             base *= base;

             n >>= 1;
         }

         if(tempn < 0) return 1/ans;
        return ans;
    }
};