class TrieNode{

    public:
        vector<TrieNode*> links;
        int isTerminal;

        TrieNode(){
            links.resize(26, NULL);
            isTerminal = 0;
        }

};


class Trie{
    public:
    TrieNode* root;
    Trie(){
        root = new TrieNode();
    }

    void insert(string word){
        TrieNode* temp = root;
        for(char c: word){
            if(!temp->links[c - 'a']){
                temp->links[c - 'a'] = new TrieNode();
            }
            temp = temp->links[c - 'a'];
        }
        temp->isTerminal++;
        
    }

    int dfs(TrieNode *root, string &s, int idx, vector<int>pos[]) {
        int res = 0;
        for (int i = 0; i < 26; i++) {
            if (root->links[i]) {
                int newIdx = upper_bound(pos[i].begin(), pos[i].end(), idx) - pos[i].begin();
                if (newIdx == pos[i].size()) continue;
                res += dfs(root->links[i], s, pos[i][newIdx], pos);
            }
        }
        return res + root->isTerminal;
    }
};



class Solution {
public:
    int numMatchingSubseq(string s, vector<string>& words) {
        Trie* trie = new Trie();

        for(string word: words){
            trie->insert(word);
        }

        vector<int> pos[26];
        for(int i = 0; i < s.length(); i++){
            pos[s[i] - 'a'].push_back(i);
        }

        return trie->dfs(trie->root, s, -1, pos);
    }
};