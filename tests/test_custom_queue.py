import unittest
from classes.stack import Node
from classes.custom_queue import Queue


class TestNode(unittest.TestCase):
    def setUp(self):
        self.queue_1 = Queue()


    def test_enqueue(self):
        """Тестирует метод enqueue"""
        self.queue_1.enqueue('data1')
        self.queue_1.enqueue('data2')
        self.queue_1.enqueue('data3')
        assert self.queue_1.head.data == 'data1'
        assert self.queue_1.head.next_node.data == 'data2'
        assert self.queue_1.tail.data == 'data3'
        assert self.queue_1.tail.next_node is None


    def test_dequeue(self):
        """Тестирует метод dequeue"""
        self.queue_1.enqueue('data1')
        self.queue_1.enqueue('data2')
        self.queue_1.enqueue('data3')
        assert self.queue_1.dequeue() == 'data1'
        assert self.queue_1.dequeue() == 'data2'
        assert self.queue_1.dequeue() == 'data3'
        assert self.queue_1.dequeue() is None







