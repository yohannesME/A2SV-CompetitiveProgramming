#include <bits/stdc++.h>
#define ll long long
using namespace std;

const int MAXN = 1000000;

struct arr {
    int a[26];
    arr() {}
    void clear() { memset(a,-1,sizeof(a)); }
    int& operator[](int i) { return a[i]; }
};

struct trie {
    int cnt, prefix_cnt[MAXN], word_cnt[MAXN];
    arr to[MAXN];

    trie() { cnt = MAXN-1; }

    void clear() { for(int i = 0; i < cnt; i++) prefix_cnt[i] = word_cnt[i] = 0, to[i].clear(); cnt = 1; }

    void add(const string& s) {
        int u = 0;
        for(const char& c: s)  {
            if(to[u][c-'a'] == -1) to[u][c-'a'] = cnt++;
            u = to[u][c-'a'];
            prefix_cnt[u]++;
        }
        word_cnt[u]++;
    }

    int prefix_count(const string& s) {
        int u = 0;
        int prefix = 0;
        for (const char& c: s) {
            if (to[u][c-'a'] == -1) return 0;
            u = to[u][c-'a'];
            prefix += prefix_cnt[u];
        }
        
        return prefix;
    }
} tr;

// int main() {
//     tr.clear();
//     string s = "codechef";
//     tr.add(s);
//     s = "codeforces";
//     tr.add(s);
//     s = "youtube";
//     tr.add(s);
//     s = "google";
//     tr.add(s);
//     s = "code"; 
//     cout<<tr.prefix_count(s)<<endl;
//     return 0;
// }




class Solution {
public:
    vector<int> sumPrefixScores(vector<string>& words) {
        tr.clear();
        vector<int> ans;

        for(string word: words){
            tr.add(word);
        }
        for (string word : words)
             ans.push_back(tr.prefix_count(word));
         return ans;
    }
};