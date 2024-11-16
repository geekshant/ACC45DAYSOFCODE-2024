class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def odd_even_list(head):
    if not head or not head.next:
        return head
    
    odd = head
    even = head.next
    even_head = even
    
    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    
    odd.next = even_head
    return head

def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def print_linked_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    print(" -> ".join(map(str, values)))

def main():
    T = int(input("Enter the number of test cases: "))
    for _ in range(T):
        arr = list(map(int, input("Enter the elements of the linked list: ").split()))
        head = create_linked_list(arr)
        new_head = odd_even_list(head)
        print_linked_list(new_head)

if __name__ == "__main__":
    main()
