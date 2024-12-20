class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

def create_linked_list(values, pos):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    cycle_node = None
    if pos == 0:
        cycle_node = head
    for i in range(1, len(values)):
        current.next = ListNode(values[i])
        current = current.next
        if i == pos:
            cycle_node = current
    if pos != -1:
        current.next = cycle_node
    return head

if __name__ == "__main__":
    # Take input from the user
    num_nodes = int(input("Enter the number of nodes in the linked list: "))
    
    if num_nodes > 0:
        values = list(map(int, input(f"Enter the {num_nodes} node values separated by spaces: ").split()))
        pos = int(input("Enter the position where the cycle starts (0-indexed, -1 for no cycle): "))
        
        # Create the linked list
        head = create_linked_list(values, pos)
        
        # Check if the linked list has a cycle
        result = hasCycle(head)
        
        print(f"Does the linked list have a cycle? {'True' if result else 'False'}")
    else:
        print("The number of nodes must be greater than 0.")
