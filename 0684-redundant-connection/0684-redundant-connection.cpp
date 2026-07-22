class DSU {
    vector<int> parent;
    vector<int> rank;

    public: 
    DSU(int n){
        for(int i=0; i<n; ++i) this->parent.push_back(i);
        this->rank.resize(n,1);
    }

    int find(int node){
        if(this->parent[node] == node) return node;
        return parent[node] = find(this->parent[node]);
    }

    bool join(int m, int n){
        int pm = this->find(m), pn = this->find(n);
        if(pm == pn) return false;
        if(this->rank[pm] < this->rank[pn]){
            int temp = pm;
            pm = pn;
            pn = temp;
        }
        this->parent[pn] = pm;
        this->rank[pm] += this->rank[pn];
        return true;
    }
};

class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        size_t e = edges.size();

        DSU* dsu = new DSU(e);

        for(const vector<int> edge : edges){
            if(!dsu->join(edge[0]-1, edge[1]-1)) return edge;
        }

        return {};
    }
};