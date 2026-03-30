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
    bool isCompleteTree(TreeNode* root) {
        if(!root || (!root->left && !root->right)) return true;

        queue<TreeNode*> bfs;
        bfs.push(root);

        while(bfs.front()){
            TreeNode* curr = bfs.front();
            bfs.pop();

            if(!curr->left && curr->right) return false;

            bfs.push(curr->left);
            bfs.push(curr->right);
        }

        while(!bfs.empty()  && !bfs.front()) bfs.pop();

        return bfs.empty();
    }
};