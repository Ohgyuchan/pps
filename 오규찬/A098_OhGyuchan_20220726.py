class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = set()
        curr = headA
        
        while curr:
            a.add(curr)
            curr=curr.next
        
        curr = headB
        while curr:
            if curr in a :
                return curr
            curr=curr.next

        return None
        