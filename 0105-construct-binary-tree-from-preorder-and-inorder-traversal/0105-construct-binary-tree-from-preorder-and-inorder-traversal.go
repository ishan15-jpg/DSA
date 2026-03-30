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
        var root *TreeNode = &TreeNode{ Val: preorder[0] }
        return root
    }

    var i int16 = 0

    var help func(int16, int16) *TreeNode
    help = func(start int16, end int16) *TreeNode {
        if start > end { return nil }

        var root *TreeNode = &TreeNode{ Val: preorder[int(i)] }

        var j int16 = start
        for j < end {
            if inorder[int(j)] == preorder[int(i)] { break }
            j++ 
        }

        i++

        root.Left = help(start, j-1)
        root.Right = help(j+1, end)

        return root
    }

    return help(0, int16(len(preorder) - 1))
}