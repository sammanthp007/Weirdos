class NodeType:
    def __init__(self):
        self.val = None
        self.lchild = None
        self.rchild = None

class BinaryTree:
    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    def breadthwise_make_tree_from_list(self, lis):
        queue = []

        # case when list is empty
        if len(lis) == 0:
            return self.head

        # create the head and add value
        self.head = NodeType()
        self.head.val = lis[0]

        current = self.head
        queue.append(current)

        for i in lis:
            current = queue.pop(0)

            current.lchild = NodeType()
            queue.append(current.lchild)

            current.rchild = NodeType()
            queue.append(current.rchild)

            current.val = i

        for node in queue:
            node = None

        queue.clear()

        return self.head

    def breadthwise_print(self):
        current = self.head
        queue = []

        if self.head == None:
            return None

        queue.append(current)

        while queue:
            current = queue.pop(0)

            if current.lchild:
                queue.append(current.lchild)

            if current.rchild:
                queue.append(current.rchild)

            if current.val != None:
                print (current.val, end=" ")

        print()


    def print_tree(self):
        current = self.head
        self.recursive_print_tree(current)
        print()

    def recursive_print_tree(self, head):
        if head.val == None:
            return
        else:
            self.recursive_print_tree(head.lchild)
            print (head.val, end=" ")
            self.recursive_print_tree(head.rchild)

