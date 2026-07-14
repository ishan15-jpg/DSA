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

        int preIdx = 0, inIdx = 0;

        function<TreeNode*(int)> dfs = [&](int limit) -> TreeNode* {
            if(preIdx >= n) return nullptr;
            if(inorder[inIdx] == limit){
                ++inIdx;
                return nullptr;
            }
            TreeNode* node = new TreeNode(preorder[preIdx]);
            node->left = dfs(preorder[preIdx++]);
            node->right = dfs(limit);

            return node;
        };

        return dfs(INT_MAX);
    }
};