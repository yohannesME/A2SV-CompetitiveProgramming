class TrieNode{

    public:
        vector<TrieNode*> links;
        bool isEnd;

        TrieNode(){
            links.resize(26, NULL);
            isEnd = false;
        }

};


class Trie{
    public:
    TrieNode* root;
    string ans;
    Trie(){
        root = new TrieNode();
        ans = "";
    }

    void insert(string word){
        TrieNode* temp = root;
        int diffCount = 0;
        for(char c : word){
            if(!temp->links[c - 'a']){
                temp->links[c - 'a'] = new TrieNode();
            }

            if(!temp->links[c - 'a']->isEnd)diffCount++;


            temp = temp->links[c - 'a'];
        }
        temp->isEnd = true;
        
        if(diffCount == 1){
            if(word.length() > ans.length()){
                ans = word;
            }else if(word.length() == ans.length() && ans > word ){
                ans = word;
            }
        }
        
    }

};




class Solution {
public:
    string longestWord(vector<string>& words) {
        sort(words.begin(), words.end());
        
        Trie* trie = new Trie();
        for(auto word : words){
            trie->insert(word);
        }
        return trie->ans;
        
    }
};