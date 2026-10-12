#code only defines the function; it doesn't call the function or print the result.
#

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val #store the node's value 
        self.next = next #pints to the next node

    def MergeTwoList(list1, list2):
        dummy = ListNode(-1) # creates a dummy list 
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:  # Fixed: list1.val
                current.next = list1
                list1 = list1.next     # Fixed: list1
            else:
                current.next = list2
                list2 = list2.next

            current = current.next     # Fixed: indentation

        current.next = list1 or list2
        return dummy.next


# Create the first linked list: 1 → 3 → 5
list1 = ListNode(1, ListNode(3, ListNode(5)))

# Create the second linked list: 2 → 4 → 6
list2 = ListNode(2, ListNode(4, ListNode(6)))

# Call the function to merge both lists
solution = ListNode()
result = solution.MergeTwoList(list1, list2)

# Print the merged list
while result:
    print(result.val, end=" → ")
    result = result.next

print("None")

"""
How the code works
Suppose the two sorted linked lists are:
list1: 1 → 3 → 5
list2: 2 → 4 → 6
The code compares the values at the heads of both lists and attaches the smaller node to the merged list.
Step-by-step merging
Initially
List 1: 1 → 3 → 5
List 2: 2 → 4 → 6
Compare and attach the smaller node
1 is smaller → 1
2 is smaller → 1 → 2
3 is smaller → 1 → 2 → 3
4 is smaller → 1 → 2 → 3 → 4
5 is smaller → 1 → 2 → 3 → 4 → 5
Final merged list
1 → 2 → 3 → 4 → 5 → 6
Why do we use dummy?
dummy = ListNode(-1) creates a temporary starting node. It makes it easier to attach nodes without separately handling the first node.
current points to the last node in the merged list.
current.next = list1 or list2 attaches all remaining nodes once one list becomes empty.
return dummy.next returns the merged list, skipping the temporary dummy node.

dummy = ListNode(-1)
"""