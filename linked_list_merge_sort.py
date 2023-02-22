from linked_list import LinkedList

# l = LinkedList()
# l.add(10)
# print(l)

def merge_sort(linked_list):
    """
    Sorts a linked list in ascending order
    Recursively divide the linked list into sublists containing a single node
    Repeatedly merge the sublists to produce sorted sublists until one remails
    Returns a sorted linked list
    """

    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list
    
    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(linked_list):
    """
    Divide the unsorted list at midpoint into sublists
    """

    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None

        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size//2


        # Start with a single linked list and find the mid point 
        mid_node = linked_list.node_at_index(mid-1) # -1 as size starts at 0
        left_half = linked_list
        # the node that comes after the mid point becomes the head of a new linked list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        # connection is removed from the mid point to new linked list
        mid_node.next_node = None

        return left_half, right_half
    
def merge(left, right):
    """
    Merges two linked lists sorting by data in the nodes
    Returns a new merged list
    """

    # Create a new LinkedList() that contains nodes from
    # merging left and right

    merged = LinkedList()

    # add a fake head that is discarded later
    merged.add(0)

    # set current to the head of the LinkedList

    current = merged.head

    # Obtain head nodes for left and right linkedlists

    left_head = left.head
    right_head = right.head

    # Iterate over left and right until we reach the tail node of either

    while left_head or right_head:
        # if the head node of left is none, we're past the tail
        # Add the node from right to merged linked list
        if left_head is None:
            current.next_node = right_head
            # call next on right to set loop condition to false
            right_head = right_head.next_node
        # if the head node of right is none, we're past the tail
        # Add the tail node from left to merged linked list
        elif right_head is None:
            current.next_node = left_head
            # Call next on left to set loop condition to false
            left_head = left_head.next_node
        else:
            # Not at either node
            # Obtain node data to perform comparison operations
            left_data = left_head.data
            right_data = right_head.data
            # if data on left is less than right, set current to left node
            if left_data < right_data:
                current.next_node = left_head
                # Move left head to next node
                left_head  = left_head.next_node
            # if data on left is greater than right, set current to right now
            else:
                current.next_node = right_head
                # Move right head to next node
                right_head = right_head.next_node
        
        # Move current to next node
        current = current.next_node

    # Discard fake head ans set firsst merged node as head
    head = merged.head.next_node
    merged.head = head

    return merged

l = LinkedList()
l.add(10)
l.add(2)
l.add(44)
l.add(15)
l.add(200)
print(l)
sorted_linked_list = merge_sort(l)
print(sorted_linked_list)
# [Head: 200]-> [15]-> [44]-> [2]-> [Tail: 10]
# [Head: 2]-> [10]-> [15]-> [44]-> [Tail: 200]