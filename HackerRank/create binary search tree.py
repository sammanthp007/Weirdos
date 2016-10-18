
class node:
    def __init__(self):
        self.val = None
        self.left = None
        self.right = None
        
        
def  createBST(keys):
    counter = 0
    tree = node()
    
    for key in keys:
        if tree.val == None:
            tree.val = key
        else:
            counter = insert(tree, key, counter)
        print (counter)
        
def insert(root, key, counter):
    counter += 1
    if key < root.val:
        if root.left == None:
            new_node = node()
            new_node.val = key
            root.left = new_node
        else:
            counter = insert(root.left, key, counter)
    else:
        if root.right == None:
            new_node = node()
            new_node.val = key
            root.right = new_node
        else:
            counter = insert(root.right, key, counter)
    return counter
