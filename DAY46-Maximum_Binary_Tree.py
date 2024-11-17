class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def construct_maximum_binary_tree(nums):
    if not nums:
        return None
    max_value = max(nums)
    max_index = nums.index(max_value)
    root = TreeNode(max_value)
    root.left = construct_maximum_binary_tree(nums[:max_index])
    root.right = construct_maximum_binary_tree(nums[max_index + 1:])
    return root

def print_tree(root, level=0, prefix="Root: "):
    if not root:
        return
    print(" " * (level * 4) + prefix + str(root.val))
    if root.left or root.right:
        if root.left:
            print_tree(root.left, level + 1, "L--- ")
        else:
            print(" " * ((level + 1) * 4) + "L--- None")
        if root.right:
            print_tree(root.right, level + 1, "R--- ")
        else:
            print(" " * ((level + 1) * 4) + "R--- None")

def main():
    nums = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
    root = construct_maximum_binary_tree(nums)
    print("The Maximum Binary Tree is:")
    print_tree(root)

if __name__ == "__main__":
    main()
