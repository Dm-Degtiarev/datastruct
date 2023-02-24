from classes.classes import Node, Stack

# Проверка-  урок 13.2 - Режимы доступа
stack = Stack()
stack.push('data1')
data = stack.pop()

print(stack.top)
print(data)

stack = Stack()
stack.push('data1')
stack.push('data2')
data = stack.pop()

print(stack.top.data)
print(data)