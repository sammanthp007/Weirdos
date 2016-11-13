import binarytree

# little flawed but its fine

def nonrecursive_constant_space_traversal(head):
    now, old = head, None

    while now != None:
        print (now.val)
        if is_leaf(now):
            now, old = now.parent, now
        else:
            if old == now.right:
                now, old = now.parent, now
            if old == now.left:
                now, old = now.right, now
            if old == now.parent:
                now, old = now.left, now

