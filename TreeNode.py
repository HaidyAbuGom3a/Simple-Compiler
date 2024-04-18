from collections import deque

class TreeNode:
    def __init__(self, identifier):
        self.identifier = identifier
        self.left = None
        self.right = None

def insert(root, identifier):
    if root is None:
        return TreeNode(identifier)
    
    if identifier < root.identifier:
        root.left = insert(root.left, identifier)
    elif identifier > root.identifier:
        root.right = insert(root.right, identifier)
    
    return root

def printTree(root):
    if root is None:
        return
    
    # Initialize a queue for level-order traversal
    queue = deque([(root, "", "root")])
    
    while queue:
        current_node, prefix, position = queue.popleft()
        
        # Print the current node with its prefix and position
        if position != "root":
            print(prefix, f"| {position} | {current_node.identifier}")
        else:
            print('root is:',current_node.identifier)
        
        # Enqueue the left child with updated prefix and position
        if current_node.left is not None:
            new_prefix = prefix + f"| {position} | "
            queue.append((current_node.left, new_prefix, "L"))
        
        # Enqueue the right child with updated prefix and position
        if current_node.right is not None:
            new_prefix = prefix + f"| {position} | "
            queue.append((current_node.right, new_prefix, "R"))