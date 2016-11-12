import binarytree

def print_all_paths_in_binary_tree(head):
    if head == None or head.val == None:
        return

    stack = []
    stack.append([head, [head.val]])

    while stack:
        current = stack.pop()
        current_node = current[0]
        current_path = current[1]

        if current_node.rchild.val == None:
            if current_node.lchild.val == None:
                print (current_path)
                continue

        if current_node.rchild.val != None:
            new_r_path = current_path[:]
            new_r_path.append(current_node.rchild.val)
            new_r_node = current_node.rchild
            stack.append([new_r_node, new_r_path])
        elif current_node.rchild.val == None:
            print(current_path)

        if current_node.lchild.val != None:
            new_l_path = current_path[:]
            new_l_path.append(current_node.lchild.val)
            new_l_node = current_node.lchild
            lnode = [new_l_node, new_l_path]
            stack.append(lnode)
        elif current_node.lchild.val == None:
            print(current_path)

lis = [3,4,5,6,7,8,9,0]
a = binarytree.BinaryTree()
a.breadthwise_make_tree_from_list(lis)

a.breadthwise_print()

print_all_paths_in_binary_tree(a.head)
