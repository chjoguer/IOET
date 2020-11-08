# Creamos la clase node
class node:
    def __init__(self, data = None, salary=None, next = None):
        self.data = data
        self.salary = salary
        self.next = next

# Creamos la clase linked_list
class linked_list: 
    def __init__(self):
        self.head = None
    
    # Método para verificar si la estructura de datos esta vacia
    def is_empty(self):
        return self.head == None

    # Método para agregar elementos al final de la linked list
    def add_at_end(self, data,salary):
        if not self.head:
            self.head = node(data=data,salary=salary)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node(data=data,salary=salary)

    # Método para imprimir la lista de nodos
    def print_list( self ):
        node = self.head
        while node != None:
            print("User:",node.data,"Amount:",node.salary,)
            node = node.next

