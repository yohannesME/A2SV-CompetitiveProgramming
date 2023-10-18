#define ll long long


class Solution {
public:
    bool prime[15000105]; 
        void sieve(int n) { 
        for (ll i = 0; i <= n; i++) prime[i] = 1;
        for (ll p = 2; p * p <= n; p++) { 
            if (prime[p] == true) { 
            for (ll i = p * p; i <= n; i += p) 
                prime[i] = false; 
            } 
        } 
        prime[1] = prime[0] = 0;
        } 
    int countPrimes(int n) {
        sieve(n);
        ll ans = 0;
        for(int i = 0; i < n; i++){
            ans += prime[i];
        }
        return ans;
    }
};