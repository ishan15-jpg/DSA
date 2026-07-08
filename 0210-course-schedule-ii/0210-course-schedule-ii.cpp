class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> adjList(numCourses);
        for(const vector<int> prerequisite : prerequisites)
        adjList[prerequisite[0]].push_back(prerequisite[1]);

        vector<bool> visited(numCourses, false);
        vector<bool> stackTrace(numCourses, false);
        vector<int> answer;

        function<bool(int)> dfs = [&](int course) -> bool {
            visited[course] = stackTrace[course] = true;
            for(const int rc : adjList[course]){
                if(visited[rc] && stackTrace[rc]) return true;
                if(!visited[rc] && dfs(rc)) return true;
            }
            stackTrace[course] = false;
            answer.push_back(course);
            return false;
        };

        for(int c=0; c<numCourses; ++c)
        if(!visited[c] && dfs(c)) return {}; 

        return answer;
    }
};