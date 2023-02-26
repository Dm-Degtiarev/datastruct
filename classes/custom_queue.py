from classes.classes import Node


class Queue:
    def __init__(self):
        """Инициализация"""
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """Добавляет данные в очередь"""
        enqueue_node = Node(data)

        if self.tail is not None:
            self.tail.next_node = enqueue_node
        else:
            self.head = enqueue_node
        self.tail = enqueue_node

