class TrieNode{
    public:
    vector<TrieNode*> children;
    int sumCount;

    TrieNode(){
        children.resize(26, NULL);
        sumCount = 0;
    }
};

class MapSum {
public:
    TrieNode* root;
    map<string, int> history;
    MapSum() {
        root = new TrieNode();
    }


    
    void insert(string key, int val) {
        TrieNode* temp = root;

        if(history.find(key) != history.end()){
            int temp = val;
            val -= history[key];
            history[key] = temp;
        } else{
        history[key] = val;
        }

        
        for(char c : key){
            if(!temp->children[c - 'a']) temp->children[c - 'a'] = new TrieNode();
            temp->children[c - 'a']->sumCount += val;
            temp = temp->children[c-'a'];
        }
        
        
    }
    
    int sum(string prefix) {
        TrieNode* temp = root;
        int value = 10000000;

        for(char c: prefix){
            if(!temp->children[c - 'a']) return 0;
            value = min(value, temp->children[c - 'a']->sumCount);
            temp =temp->children[c - 'a'];
        }

        return value;
    }
};

/**
 * Your MapSum object will be instantiated and called as such:
 * MapSum* obj = new MapSum();
 * obj->insert(key,val);
 * int param_2 = obj->sum(prefix);
 */