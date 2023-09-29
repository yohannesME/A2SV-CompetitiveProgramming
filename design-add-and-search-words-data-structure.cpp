class TrieNode{
    public:
    std::unordered_map<char, TrieNode*> children;
    bool isEnd;
};

class WordDictionary {
public:
    TrieNode* root;
    WordDictionary() {
        root = new TrieNode();
    }
    
    void addWord(string word) {
        TrieNode* temp = root;

        for(char c: word){
            if(temp->children.find(c) == temp->children.end()){
                temp->children[c] = new TrieNode();
            }
            temp = temp->children[c];
        }
        temp->isEnd = true;
    }
    
    bool searchstr(string word, TrieNode* temp, int i) {
        if(i == word.length()-1){
            if(word[i] == '.'){
                for(auto node : temp->children){
                    if(node.second->isEnd) return true;
                }
            }else{
                if(temp->children.find(word[i]) != temp->children.end()) return temp->children[word[i]]->isEnd;
                return false;
            }
        }

        if(word[i] == '.')
            for(auto node: temp->children){
                if(searchstr(word, node.second, i+1)) return true;
            }

        if(temp->children.find(word[i]) == temp->children.end())return false;

        return searchstr(word, temp->children[word[i]], i+1);
    }

    bool search(string word){
        return searchstr(word, root, 0);
    }
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */