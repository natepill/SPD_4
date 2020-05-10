
class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = None

"""
Q1:
Given a singly-linked list, reverse the order of the list by modifying the nodes’ links.
"""

def reverse_LL(curr_node):
    past_node = None

    while curr_node is not None:
        # print(curr_node.data)
        next_node = curr_node.next
        curr_node.next = past_node
        past_node = curr_node
        curr_node = next_node



    return past_node


"""
Q2:
Rotate a given singly-linked list counter-clockwise by k nodes, where k is a given integer.
Example: If the given linked list is
A → B → C → D → E → F and k is 4, nodes should be modified so the list becomes
E → F → A → B → C → D.

Assumptions: k is positive and smaller than n, the length of the linked list.
"""


def counter_clock_rotate(node):
"""
    Save head of LL
    Traverse to Kth node from head of list
    save Kth+1 node
    point kth node from head to None
    Traverse From kth+1 node to end
    Point last node towards saved head of list
"""

    head = node
    curr_node = node

    for _ in range(k-1):
        curr_node = curr_node.next

    new_list_head = curr_node.next
    curr_node.next = None

    while new_list_head.next is not None:
        new_list_head = new_list_head.next

    new_list_head.next = head

if __name__ == "__main__":
    node3 = Node("C")
    node2 = Node("B")
    node1 = Node("A")

    node = node1
    node1.next = node2
    node2.next = node3

    # print(node1.next)

    while node is not None:
        # print(node.data)
        # print(node.next)
        node = node.next

    #
    reverse_LL(node1)
    #
    test_reverse_node = node3
    #
    while test_reverse_node is not None:
        print(test_reverse_node.data)
        test_reverse_node = test_reverse_node.next
