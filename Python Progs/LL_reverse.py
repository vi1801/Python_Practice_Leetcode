class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val})"


def fn(head):
    curr = head
    prev = None
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node 

    # Return the new head (prev) after the list is reversed
    return prev


def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    print()  # Newline for formatting


if __name__ == "__main__":
    # Create and print the original linked list
    head = create_linked_list([1, 2, 3, 4, 5])
    print("Original linked list:")
    print_linked_list(head)
    
    # Reverse the linked list and print it
    reversed_head = fn(head)
    print("Reversed linked list:")
    print_linked_list(reversed_head)
