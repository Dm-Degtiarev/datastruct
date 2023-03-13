class Node:
    def __init__(self, data: dict, next_node=None):
        """
        Инициализация
        :param data: словарь с данными
        :param next_node: ссылка на следующий узел
        """
        self.data = data
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        """
        Инициализация
        :param data_dict: словарь с данными
        :param next_node: ссылка на следующий узел
        """
        self.left = None
        self.right = None

    def insert_beginning(self, node):
        """Добавляет словарь в начало"""
        ll_node = Node(node)
        if self.left is None:
            self.left = ll_node
            self.right = ll_node
        else:
            ll_node.next_node = self.left
            self.left = ll_node

    def insert_at_end(self, node):
        """Добавляет словарь в конец"""
        ll_node = Node(node)
        if self.right is None:
            self.left = ll_node
            self.right = ll_node
        else:
            self.right.next_node = ll_node
            self.right = ll_node

    def print_ll(self):
        """Выводит в консоль / возвращает цепочку списка"""
        ll_string = ''
        node = self.left
        if node is None:
            print(None)
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        print(ll_string)
        return ll_string

    def to_list(self):
        """Возвращает элементы односвязного списка в виде списка"""
        ll_list = list()
        node = self.left

        while node:
            ll_list.append(node.data)
            node = node.next_node

        return  ll_list

    def get_data_by_id(self, inp_value):
        """Возвращает первый элемент списка, где значение id = inp_value"""
        try:
            for dict in self.to_list():
                if dict['id'] == inp_value:
                    return dict
                    break
        except TypeError:
            print('Данные не являются словарем или в словаре нет id')


