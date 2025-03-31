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
int res=0;
public:
    
    int depthOfTree(TreeNode* root){
        if(!root){
            return 0;
        }
        int l = depthOfTree(root->left);
        int r = depthOfTree(root->right);
        
        res = max(res, l+r);

        
        return 1+max(l, r);
    }
    
    int diameterOfBinaryTree(TreeNode* root) {
        depthOfTree(root);
        return res;
    }
};