class DSU{
    public:
    int size = 0;
    vector<int> parent;
    DSU(int n){
        parent = vector<int>(n);

        for(int i = 0; i < n; i++){
            parent[i] = i;
        }
    }

    int find(int x){
        if(parent[x] == x) return x;
        parent[x] = find(parent[x]);
        return parent[x];
    }

    void merge(int u, int v){
        int up = find(u);
        int vp = find(v);

        // if(up == 0 || vp == 0){
        //     parent[up] = 0;
        //     parent[vp] = 0;
        // }else
        parent[up] = vp;
    }

    bool isConnected(int u, int v){
        return find(u) == find(v);
    }


    
};

class Solution {
public:
    vector<int> findAllPeople(int n, vector<vector<int>>& meetings, int firstPerson) {
        DSU* dsu = new DSU(n);
        map<int , vector<vector<int>>> timed;

        for(auto meet : meetings){
            timed[meet[2]].push_back({meet[0], meet[1]});
        }

        vector<int> ans;
        dsu->merge(0, firstPerson);

        for(auto time : timed){

            for(auto ppl : time.second){
                dsu->merge(ppl[0], ppl[1]);
            }

            for(auto ppl : time.second){

                if(dsu->find(ppl[1]) != dsu->find(0) && dsu->find(ppl[0]) != dsu->find(0)){
                    dsu->parent[ppl[0]] = ppl[0];
                    dsu->parent[ppl[1]] = ppl[1];
                }
            }
        }

        for(int i = 0; i < n; i++)
            if(dsu->find(i) == dsu->find(0))ans.push_back(i);


        return ans;
    }
};