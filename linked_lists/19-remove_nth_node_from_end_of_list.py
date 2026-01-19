#19. Remove Nth Node From End of List
#Medium
#
#Given a linked list, remove the n-th node from the end of list and return its head.
#
#Example:
#
#Given linked list: 1->2->3->4->5, and n = 2.
#
#After removing the second node from the end, the linked list becomes 1->2->3->5.
#
#Note:
#
#Given n will always be valid.
#
#Follow up:
#
#Could you do this in one pass?
#
#
#
#
#
#



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        left_pt = head
        right_pt = left_pt
        for i in range(n+1):
            if (not right_pt.next) and (i != n):
                return head.next
            right_pt = right_pt.next
        while right_pt is not None:
            left_pt = left_pt.next
            right_pt = right_pt.next
        left_pt.next = left_pt.next.next
        return head


public ListNode removeNthFromEnd(ListNode head, int n) {
    ListNode dummy = new ListNode(0);
    dummy.next = head;
    int length  = 0;
    ListNode first = head;
    while (first != null) {
        length++;
        first = first.next;
    }
    length -= n;
    first = dummy;
    while (length > 0) {
        length--;
        first = first.next;
    }
    first.next = first.next.next;
    return dummy.next;
}



public ListNode removeNthFromEnd(ListNode head, int n) {
    ListNode dummy = new ListNode(0);
    dummy.next = head;
    ListNode first = dummy;
    ListNode second = dummy;
    // Advances first pointer so that the gap between first and second is n nodes apart
    for (int i = 1; i <= n + 1; i++) {
        first = first.next;
    }
    // Move first to the end, maintaining the gap
    while (first != null) {
        first = first.next;
        second = second.next;
    }
    second.next = second.next.next;
    return dummy.next;
}
