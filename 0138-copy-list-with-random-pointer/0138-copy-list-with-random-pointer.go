/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Next *Node
 *     Random *Node
 * }
 */

func copyRandomList(head *Node) *Node {
    if head == nil { return nil }
    curr := head
    for curr != nil {
        copy := Node{curr.Val,nil,nil}
        copy.Next = curr.Next
        curr.Next = &copy
        curr = curr.Next.Next
    }
    curr = head 
    for curr != nil {
        temp := curr.Next
        if curr.Random != nil {
            temp.Random = curr.Random.Next
        }
        curr = curr.Next.Next
    }
    newHead := head.Next
    curr = head 
    for curr != nil {
        temp := curr.Next
        curr.Next = temp.Next
        if temp.Next != nil {
            temp.Next = temp.Next.Next
        }
        curr = curr.Next
    }
    return newHead
}