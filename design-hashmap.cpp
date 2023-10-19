class MyHashMap {
public:
    map<int, int> hashmap;
    MyHashMap() {
       
    }
    
    void put(int key, int value) {
        hashmap[key] = value;
    }
    
    int get(int key) {
        if(hashmap.find(key) == hashmap.end())return -1;
        return hashmap.find(key)->second;
    }
    
    void remove(int key) {
        if(hashmap.find(key) != hashmap.end())
        hashmap.erase(hashmap.find(key));
    }
};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */