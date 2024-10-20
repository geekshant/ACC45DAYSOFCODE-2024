class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy_head = ListNode(0)
    current = dummy_head
    carry = 0

    while l1 or l2 or carry:
        sum_val = carry
        if l1:
            sum_val += l1.val
            l1 = l1.next
        if l2:
            sum_val += l2.val
            l2 = l2.next
        carry = sum_val // 10
        current.next = ListNode(sum_val % 10)
        current = current.next

    return dummy_head.next

def create_linked_list(digits):
    dummy_head = ListNode(0)
    current = dummy_head
    for digit in digits:
        current.next = ListNode(digit)
        current = current.next
    return dummy_head.next

def print_linked_list(l):
    digits = []
    while l:
        digits.append(str(l.val))
        l = l.next
    return ' -> '.join(digits)

def main():
    # Take input for the first linked list
    digits1 = list(map(int, input("Enter the digits for the first number in reverse order, separated by spaces: ").split()))
    l1 = create_linked_list(digits1)

    # Take input for the second linked list
    digits2 = list(map(int, input("Enter the digits for the second number in reverse order, separated by spaces: ").split()))
    l2 = create_linked_list(digits2)

    # Add the two numbers
    result = addTwoNumbers(l1, l2)

    # Print the resulting linked list
    print("The sum is:", print_linked_list(result))

if __name__ == "__main__":
    main()
