class Node:
    def __init__(self, data, next_node=None):
        """
        Инициализация
        :param data: любые полезные данные: число, строка, список и т.д
        :param next_node: ссылка на следующий узел
        """
        self.data = data
        self.next_node = next_node


class Stack():
    def __init__(self, top=None):
        """
        Инициализация
        :param top: ссылка на верхний (крайний в стэке) узел
        """
        self.top = top


    def push(self, node):
        """
        Добавляет данные в стек
        :param node: объект класса Node
        """
        curr_top = self.top
        self.top = Node(node)
        self.top.next_node = curr_top
