class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def connect(root):
    if not root:
        return None
    
    queue = [root]
    while queue:
        next_level = []
        for i in range(len(queue)):
            node = queue[i]
            if i + 1 < len(queue):
                node.next = queue[i + 1]
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        queue = next_level
    return root

def build_tree(values):
    if not values:
        return None
    
    root = Node(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if values[i] is not None:
            node.left = Node(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = Node(values[i])
            queue.append(node.right)
        i += 1
    return root

def print_tree_next(root):
    if not root:
        return
    level = [root]
    while level:
        next_level = []
        for node in level:
            print(node.val, end=" -> " if node.next else " -> NULL\n")
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        level = next_level

def main():
    values = list(map(int, input("Enter the values for the nodes of the binary tree in level-order, separated by spaces (use -1 for NULL): ").split()))
    values = [val if val != -1 else None for val in values]
    
    root = build_tree(values)
    connect(root)
    
    print("The tree after connecting next pointers:")
    print_tree_next(root)

if __name__ == "__main__":
    main()
