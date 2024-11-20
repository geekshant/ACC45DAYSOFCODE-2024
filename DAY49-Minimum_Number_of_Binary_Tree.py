from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def min_depth(root):
    if not root:
        return 0

    queue = deque([(root, 1)])  # (node, depth)

    while queue:
        node, depth = queue.popleft()

        # If we reach a leaf node
        if not node.left and not node.right:
            return depth

        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))

def build_tree(values):
    if not values:
        return None

    nodes = [TreeNode(val) if val is not None else None for val in values]

    for i in range(len(values)):
        if values[i] is not None:
            if 2 * i + 1 < len(values):
                nodes[i].left = nodes[2 * i + 1]
            if 2 * i + 2 < len(values):
                nodes[i].right = nodes[2 * i + 2]
                
    return nodes[0]

def main():
    values = list(map(int, input("Enter the node values separated by spaces (use -1 for None): ").split()))
    values = [val if val != -1 else None for val in values]
    
    root = build_tree(values)
    
    result = min_depth(root)
    print(result)

if __name__ == "__main__":
    main()
