/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func help(root1 *TreeNode, root2 *TreeNode) {
    root1.Val = root1.Val + root2.Val
    if root1.Left != nil && root2.Left != nil { help(root1.Left,root2.Left) }
    if root1.Right != nil && root2.Right != nil { help(root1.Right,root2.Right) }
    if root1.Left == nil {
        root1.Left = root2.Left
        root2.Left = nil 
    }
    if root1.Right == nil {
        root1.Right = root2.Right
        root2.Right = nil
    }
}

func mergeTrees(root1 *TreeNode, root2 *TreeNode) *TreeNode {
    if root1 == nil || root2 == nil {
        if root1 != nil { return root1 } else { return root2 }
    }
    help(root1,root2)
    return root1
}