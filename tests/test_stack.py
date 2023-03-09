import unittest
from classes.stack import Node, Stack


class TestNode(unittest.TestCase):
    def setUp(self):
        self.node_1 = Node(1)


    def test_node_init(self):
        """Теcтсирует инициализацию Node"""
        assert self.node_1.data == 1
        assert self.node_1.next_node is None


    def test_node_next_node(self):
        """Теcтсирует next_node"""
        node_2 = Node(220, self.node_1)
        assert node_2.next_node is self.node_1


class TestStack(unittest.TestCase):
    def setUp(self) -> None:
        self.stack_1 = Stack(1)
        self.stack_2 = Stack()
        self.stack_3 = Stack()


    def test_stack_init(self):
        """Тестирует инициализацию Stack"""
        assert self.stack_1.top == 1
        assert self.stack_2.top is None


    def test_stack_push(self):
        """Тестирует работу метода push"""
        self.stack_2.push(1)
        self.stack_2.push(2)
        self.stack_2.push(3)
        assert self.stack_2.top.data == 3
        assert self.stack_2.top.next_node.data == 2
        assert self.stack_2.top.next_node.next_node.data == 1


    def test_stack_push(self):
        """Тестирует работу метода pop"""
        self.stack_2.push('data1')
        data = self.stack_2.pop()
        assert self.stack_2.top is None
        assert data == 'data1'

        self.stack_3.push('data1')
        self.stack_3.push('data2')
        data = self.stack_3.pop()
        assert self.stack_3.top.data == 'data1'
        assert data == 'data2'
