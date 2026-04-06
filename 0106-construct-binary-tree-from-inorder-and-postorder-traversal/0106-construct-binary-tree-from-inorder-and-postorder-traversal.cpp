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
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        size_t n = inorder.size();

        unordered_map<int,int> inorder_map;
        for(int i=0; i<n; i++) inorder_map[inorder[i]] = i;

        function<TreeNode*(int,int)> help = [&](int start, int end) -> TreeNode* {
            if(start > end) return nullptr;

            const int root_val = postorder.back(); postorder.pop_back();
            TreeNode* root = new TreeNode(root_val);

            const int idx = inorder_map[root_val];

            root->right = help(idx+1, end);
            root->left = help(start, idx-1);

            return root;
        };

        return help(0, n-1);
    }
};