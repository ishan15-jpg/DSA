class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        size_t e = edges.size();

        vector<vector<int>> adjList(e);
        vector<int> indegree(e, 0);
        for(const vector<int> edge : edges){
            adjList[edge[0]-1].push_back(edge[1]-1);
            adjList[edge[1]-1].push_back(edge[0]-1);
            ++indegree[edge[0]-1];
            ++indegree[edge[1]-1];
        }

        queue<int> q;
        for(int i=0; i<e; ++i) if(indegree[i] == 1) q.push(i);

        while(!q.empty()){
            int node = q.front(); q.pop();
            for(const int neigh : adjList[node]){
                --indegree[neigh];
                if(indegree[neigh] == 1) q.push(neigh);
            }
        }

        reverse(edges.begin(), edges.end()); 

        for(const vector<int> edge : edges){
            if(indegree[edge[0]-1] > 1 && indegree[edge[1]-1] > 1) return edge;
        }

        return {};
    }
};