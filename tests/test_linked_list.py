import unittest
from classes.linked_list import Node, LinkedList


class TestNode(unittest.TestCase):
    def test_node_init(self):
        """Теcтсирует инициализацию Node"""
        node_1 = Node({'1': 1})
        assert node_1.data == {'1':1}

class TestLinkedList(unittest.TestCase):
    def test_insert_beginning(self):
        """Теcтсирует insert_beginning"""
        node_1 = LinkedList()
        node_1.insert_beginning({'1':1})
        assert node_1.right.data == node_1.left.data == {'1':1}
        node_1.insert_beginning({'1': 2})
        assert node_1.right.data == {'1':1}
        assert node_1.left.data == {'1': 2}
        assert node_1.left.next_node.data == {'1': 1}


    def test_insert_at_end(self):
        """Теcтсирует insert_at_end"""
        node_1 = LinkedList()
        node_1.insert_at_end({'1':1})
        assert node_1.right.data == node_1.left.data == {'1': 1}
        node_1.insert_at_end({'1': 2})
        assert node_1.right.data == {'1': 2}
        assert node_1.left.data == {'1': 1}
        assert node_1.left.next_node.data == {'1': 2}


    def test_print_ll(self):
        """Теcтсирует print_ll"""
        node_1 = LinkedList()
        node_1.insert_beginning({'id': 1})
        node_1.insert_at_end({'id': 2})
        node_1.insert_at_end({'id': 3})
        node_1.insert_beginning({'id': 0})
        x = node_1.print_ll()
        assert x == " {'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None"


    def test_to_list(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
        ll.insert_beginning({'id': 0, 'username': 'serebro'})

        lst = ll.to_list()
        assert lst[0] == {'id': 0, 'username': 'serebro'}
        assert lst[1] == {'id': 1, 'username': 'lazzy508509'}
        assert lst[2] == {'id': 2, 'username': 'mik.roz'}
        assert lst[3] == {'id': 3, 'username': 'mosh_s'}


    def test_get_data_by_id(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
        ll.insert_beginning({'id': 0, 'username': 'serebro'})
        ll.insert_at_end('idusername')

        user_data = ll.get_data_by_id(3)
        assert user_data == {'id': 3, 'username': 'mosh_s'}

        user_data = ll.get_data_by_id(4)
        assert user_data is None




