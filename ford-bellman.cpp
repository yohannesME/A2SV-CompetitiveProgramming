#include<bits/stdc++.h>

#define lli long long int

using namespace std;



int main(){


    lli n, m;
    cin >> n >> m;

    vector<vector<lli>> graph;
    for(int i = 0; i < m; i++){
        lli v,u,w;
        cin >> v >> u >> w;

        graph.push_back({v-1, u-1, w});
    }

    lli MAX_VAL = 1e9;

    vector<lli> ans(n, MAX_VAL);
    ans[0] = 0;

    for(int k = 0; k < n-1; k++){
        for(auto edge: graph){
            lli u = edge[0];
            lli v = edge[1];
            lli w = edge[2];

            if(ans[u] != MAX_VAL && ans[u] + w < ans[v]){
                ans[v] = ans[u] + w;
            }
        }
    }

    for(auto num : ans){
        if(num == MAX_VAL)
            cout << 30000 << " ";
        else cout << num << " ";
    }
    

    return 0;
}