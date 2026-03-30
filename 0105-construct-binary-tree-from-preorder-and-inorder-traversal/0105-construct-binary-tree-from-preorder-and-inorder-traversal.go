/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func buildTree(preorder []int, inorder []int) *TreeNode {
    if len(preorder) == 1 { 
        root := TreeNode{ Val: preorder[0] }
        return &root
    }

    var i int = 0

    var help func(int, int) *TreeNode
    help = func(start int, end int) *TreeNode {
        if start > end { return nil }

        var root *TreeNode = &TreeNode{ Val: preorder[i] }

        var j int = start
        for j < end {
            if inorder[j] == preorder[i] { break }
            j++ 
        }

        i++

        root.Left = help(start, j-1)
        root.Right = help(j+1, end)

        return root
    }

    return help(0, len(preorder) - 1)
}