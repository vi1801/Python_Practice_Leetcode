class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val})"


def find_middle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow  # Return the middle node


def detect_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True  # Cycle detected

    return False  # No cycle


def cycle_length(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:  # Cycle detected
            current = slow
            length = 1
            while current.next != slow:
                current = current.next
                length += 1
            return length  # Length of the cycle

    return 0  # No cycle


# Helper function to create a linked list from a list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# Helper function to add a cycle to a linked list
def add_cycle(head, pos):
    if pos == -1:
        return head

    cycle_start = None
    current = head
    i = 0
    while current.next:
        if i == pos:
            cycle_start = current
        current = current.next
        i += 1
    current.next = cycle_start  # Creates the cycle

    return head


if __name__ == "__main__":
    # Create a linked list 1 -> 2 -> 3 -> 4 -> 5
    head = create_linked_list([1, 2, 3, 4, 5])

    # Find the middle of the linked list
    middle = find_middle(head)
    print(f"Middle node: {middle}")

    # Check for cycle in the list (without any cycle)
    print(f"Cycle detected: {detect_cycle(head)}")

    # Add a cycle to the linked list (e.g., 5 -> 3)
    head_with_cycle = add_cycle(head, pos=2)
    print(f"Cycle detected: {detect_cycle(head_with_cycle)}")

    # Get the length of the cycle
    print(f"Cycle length: {cycle_length(head_with_cycle)}")
