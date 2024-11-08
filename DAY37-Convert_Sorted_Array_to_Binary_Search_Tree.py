class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
    if not nums:
        return None

    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid + 1:])
    
    return root

def pre_order_traversal(root):
    if root:
        print(root.val, end=" ")
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)

def main():
    nums = list(map(int, input("Enter the sorted integer array separated by spaces: ").split()))
    bst_root = sortedArrayToBST(nums)
    
    print("Pre-order traversal of the height-balanced BST:")
    pre_order_traversal(bst_root)
    print()

if __name__ == "__main__":
    main()
