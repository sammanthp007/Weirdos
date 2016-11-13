class NodeType:
    def __init__(self):
        self.val = None
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def print_linked_list(self):
        current = self.head
        while current:
            print(current.val, end=' ')
            current = current.next
        print()

    def reverse_linked_list(self):
        head = self.head
        prev = None
        next_node = head.next
        while next_node:
            head.next = prev
            prev = head
            head = next_node
            next_node = next_node.next
        head.next = prev
        self.head = head

def make_linked_list_from_list(lis):
    head = NodeType()
    if len(lis) == 0:
        return head

    current = head
    current.val = lis[0]
    for i in range(1, len(lis)):
        new_node = NodeType()
        new_node.val = lis[i]
        current.next = new_node
        current = new_node

    ll = SinglyLinkedList()
    ll.head = head
    return ll

def main():
    lis = [1,2,3,4,5,6,7,8]
    ll = make_linked_list_from_list(lis)
    ll.print_linked_list()
    ll.reverse_linked_list()
    ll.print_linked_list()

main()
