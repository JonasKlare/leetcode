# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#This is really annoying because it's not an array and instead a list node. Funk this. 
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sortedHead = None
        
        while(head is not None):
            next = head.next
            head.next = None
            
            if sortedHead is None: 
                sortedHead = head
            elif sortedHead.val > head.val:
                head.next = sortedHead
                sortedHead = head
            else:
                curr = sortedHead

                while (curr.next is not None and curr.next.val < head.val):
                    curr = curr.next
                head.next = curr.next
                curr.next = head
                
            head=next
        return sortedHead
            
    
        
            

def printList(head):
    curr = head

    print(curr.val, end=" ")
    while(curr.next is not None):
        print(curr.next.val, end=" ")
        curr=curr.next

    print(" ")

