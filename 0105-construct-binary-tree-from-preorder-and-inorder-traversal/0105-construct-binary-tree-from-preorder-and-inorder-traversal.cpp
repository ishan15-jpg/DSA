/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        size_t n = preorder.size();

        int i = 0;
        unordered_map<int,int> mp;
        for(int i=0; i<n; ++i) mp[inorder[i]] = i;

        function<TreeNode*(int,int)> dfs = [&](int l, int r) -> TreeNode* {
            if(i == n || l > r) return nullptr;

            int j = mp[preorder[i]];
            TreeNode* node = new TreeNode(preorder[i++]);
            node->left = dfs(l,j-1);
            node->right = dfs(j+1,r);

            return node;
        };

        return dfs(0,n-1);
    }
};