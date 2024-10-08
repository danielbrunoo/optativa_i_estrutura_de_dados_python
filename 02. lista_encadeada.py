class ItemLista:
    def __init__(self, data=0, nextItem=None):
        self.data = data
        self.next = nextItem

    def __repr__(self):
        return '%s => %s' % (self.data, self.next)


class ListaEncadeada:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return "%s" % (self.head)

    def insere(lista, data):
        # cria um objeto para armazenar um novo item da lista
        item = ItemLista(data)
        # o head é apontado como próximo item
        item.next = lista.head
        # o item atual se torna o head
        lista.head = item

    def remove(lista, valor):
        # verifica se o item a ser removido é o head
        if lista.head and lista.head.data == valor:
            lista.head = lista.head.next
        else:
        # detecta a oposição do elemento
            before = None
            navegar = lista.next

        #print(navegar.data)
        # remove o item se ele for encontrado
        if navegar:
            before.next = navegar.next

    def busca(lista, valor):
        navegar = lista.head
        while navegar and navegar.data != valor:
            navegar = navegar.next
        return navegar

# Como utilizar este código:

lista = ListaEncadeada()
lista.insere(1)
lista.insere(2)
lista.insere(3)

print("Lista após inserções:", lista)

lista.remove(2)
print("Lista após remover o valor 2:", lista)

item_encontrado = lista.busca(3)
if item_encontrado:
    print("Item encontrado:", item_encontrado)
else:
    print("Item não encontrado.")