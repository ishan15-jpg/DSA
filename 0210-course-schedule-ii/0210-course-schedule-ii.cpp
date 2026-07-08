class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> adjList(numCourses);
        vector<int> indegree(numCourses, 0);
        for(const vector<int> prerequisite : prerequisites){
            adjList[prerequisite[0]].push_back(prerequisite[1]);
            ++indegree[prerequisite[1]];
        }

        queue<int> q;
        for(int c=0; c<numCourses; ++c) 
        if(indegree[c] == 0) q.push(c);

        vector<int> answer;

        while(!q.empty()){
            int c = q.front(); q.pop();
            answer.push_back(c);
            for(const int rc : adjList[c]){
                --indegree[rc];
                if(indegree[rc] == 0) q.push(rc);
            }
        }

        if(answer.size() < numCourses) return {};

        reverse(answer.begin(), answer.end());

        return answer;
    }
};