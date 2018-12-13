#!/usr/bin/env python3


class Node:

    def __init__(self, index):
        self.index = index
        self.nextNode = None
        self.prevNode = None
        self.prev_1000 = None
        self.prev_100 = None
        self.prev_10 = None
        self.next_1000 = None
        self.next_100 = None
        self.next_10 = None

class IndexedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.indexed = False

    def insert(self, index):
        """Insere na lista um nodo com o indice especificado no argumento, caso ja nao exista na lista"""
        self.indexed = False
        node = Node(index)
        if self.head is None:
            self.head = self.tail = node
            self.size += 1
        elif self.tail.index < index:
            node.prevNode = self.tail
            self.tail.nextNode = node
            self.tail = node
            self.tail.prev_1000 = self.tail.prevNode.prev_1000
            self.tail.prev_100 = self.tail.prevNode.prev_100
            self.tail.prev_10 = self.tail.prevNode.prev_10
            if self.tail.prevNode.prev_10:
                self.tail.prevNode.prev_1000.next_1000 = self.tail
                self.tail.prevNode.prev_100.next_100 = self.tail
                self.tail.prevNode.prev_10.next_10 = self.tail
                self.tail.prevNode.prev_1000 = None
                self.tail.prevNode.prev_100 = None
                self.tail.prevNode.prev_10 = None
            self.size += 1
        elif self.head.index > index:
            node.nextNode = self.head
            self.head.prevNode = node
            self.head = node
            self.head.next_1000 = self.head.nextNode.next_1000
            self.head.next_100 = self.head.nextNode.next_100
            self.head.next_10 = self.head.nextNode.next_10
            if self.head.nextNode.next_10:
                self.head.nextNode.next_1000.prev_1000 = self.head
                self.head.nextNode.next_100.prev_100 = self.head
                self.head.nextNode.next_10.prev_10 = self.head
                self.head.nextNode.next_1000 = None
                self.head.nextNode.next_100 = None
                self.head.nextNode.next_10 = None
            self.size += 1
        else:
            current = self.head
            reverse_search = False
            if (index - self.head.index) > (self.tail.index - index):
                reverse_search = True
                current = self.tail
            while current:
                print(current.index)
                # busca iterando sobre a lista e pulando nodos a direita do nodo de iteracao (current)
                if not reverse_search:
                    if current.next_1000:
                        while current.next_1000.index <= index:
                            current = current.next_1000
                        if (index - current.index) > (current.next_1000.index - index):
                            current = current.next_1000
                            reverse_search = True
                            continue
                    if current.next_100:
                        while current.next_100.index <= index:
                            current = current.next_100
                        if (index - current.index) > (current.next_100.index - index):
                            current = current.next_100
                            reverse_search = True
                            continue
                    if current.next_10:
                        while current.next_10.index <= index:
                            current = current.next_10
                    if current.nextNode:
                        while current.nextNode.index <= index:
                            current = current.nextNode
                        if current.index <= index:
                            break
                # busca iterando sobre a lista e pulando nodos a esquerda do nodo de iteracao (current)
                else:
                    if current.prev_1000:
                        while current.prev_1000.index >= index:
                            current = current.prev_1000
                        if (current.index - index) > (index - current.prev_1000.index):
                            current = current.prev_1000
                            reverse_search = False
                            continue
                    if current.prev_100:
                        while current.prev_100.index >= index:
                            current = current.prev_100
                        if (current.index - index) > (index - current.prev_100.index):
                            current = current.prev_100
                            reverse_search = False
                            continue
                    if current.prev_10:
                        while current.prev_10.index >= index:
                            current = current.prev_10
                    if current.prevNode:
                        while current.index > index:
                            current = current.prevNode
                        if current.index <= index:
                            break
                        #if current.prevNode.index >= index:
                        #    current = current.prevNode
                        #    # devido a busca em sentido contrario e necessario avancar o nodo de iteracao mais uma vez para a esquerda
                        #if current.prevNode.index < index:
                        #    current = current.prevNode
                        #    break
            if current.index == index:
                raise Exception('A lista ja possui um nodo com esse indice')
            node.nextNode = current.nextNode
            node.prevNode = current
            current.nextNode.prevNode = node
            current.nextNode = node
            self.size += 1

    def re_index(self):
        """Caso tenha sido realizada insercao ou remocao na lista, metodo de busca (search) chama este metodo para indexar a lista novamente"""
        self.indexed = True
        current = self.head
        prev_jump_1000 = current
        prev_jump_100 = current
        prev_jump_10 = current
        position = 1
        while current:
            if position % 1000 == 0:
                prev_jump_1000.next_1000 = current
                current.prev_1000 = prev_jump_1000
                prev_jump_1000 = current
            else:
                prev_jump_1000.next_1000 = None
                current.prev_1000 = None
                current.next_1000 = None
            if position % 100 == 0:
                prev_jump_100.next_100 = current
                current.prev_100 = prev_jump_100
                prev_jump_100 = current
            else:
                prev_jump_100.next_100 = None
                current.prev_100 = None
                current.next_100 = None
            if position % 10 == 0:
                prev_jump_10.next_10 = current
                current.prev_10 = prev_jump_10
                prev_jump_10 = current
            else:
                prev_jump_10.next_10 = None
                current.prev_10 = None
                current.next_10 = None
            if current == self.tail:
                prev_jump_1000.next_1000 = current
                prev_jump_100.next_100 = current
                prev_jump_10.next_10 = current
                current.prev_1000 = prev_jump_1000
                current.prev_100 = prev_jump_100
                current.prev_10 = prev_jump_10
            current = current.nextNode
            position += 1

    def empty(self):
        return self.size == 0

    def search(self, index):
        """Busca na lista pelo nodo com indice especificado no argumento"""
        if not self.empty():
            if not self.indexed:
                self.re_index()
            if self.head.index == index:
                return self.head
            elif self.tail.index == index:
                return self.tail
            elif self.head.index > index > self.tail.index:
                raise Exception('Indice fora dos limites da lista')
            #elif self.head.index > index > self.tail.index:
            #    raise Exception('A lista nao possui um nodo com esse indice')
            else:
                current = self.head
                reverse_search = False
                if (index - self.head.index) > (self.tail.index - index):
                    reverse_search = True
                    current = self.tail
                while current:
                    # busca iterando sobre a lista e pulando nodos a direita do nodo de iteracao (current)
                    if not reverse_search:
                        if current.next_1000:
                            while current.next_1000.index <= index:
                                current = current.next_1000
                            if (index - current.index) > (current.next_1000.index - index):
                                current = current.next_1000
                                reverse_search = True
                                continue
                        if current.next_100:
                            while current.next_100.index <= index:
                                current = current.next_100
                            if (index - current.index) > (current.next_100.index - index):
                                current = current.next_100
                                reverse_search = True
                                continue
                        if current.next_10:
                            while current.next_10.index <= index:
                                current = current.next_10
                        if current.nextNode:
                            while current.nextNode.index <= index:
                                current = current.nextNode
                            if current.index <= index:
                                break
                    # busca iterando sobre a lista e pulando nodos a esquerda do nodo de iteracao (current)
                    else:
                        if current.prev_1000:
                            while current.prev_1000.index >= index:
                                current = current.prev_1000
                            if (current.index - index) > (index - current.prev_1000.index):
                                current = current.prev_1000
                                reverse_search = False
                                continue
                        if current.prev_100:
                            while current.prev_100.index >= index:
                                current = current.prev_100
                            if (current.index - index) > (index - current.prev_100.index):
                                current = current.prev_100
                                reverse_search = False
                                continue
                        if current.prev_10:
                            while current.prev_10.index >= index:
                                current = current.prev_10
                        if current.prevNode:
                            while current.index > index:
                                current = current.prevNode
                            if current.index <= index:
                                break
                            #if current.prevNode.index >= index:
                            #    current = current.prevNode
                            #    # devido a busca em sentido contrario e necessario avancar o nodo de iteracao mais uma vez para a esquerda
                            #if current.prevNode.index < index:
                            #    current = current.prevNode
                            #    break
                if current.index == index:
                    return current
                else:
                    raise Exception('A lista nao possui um nodo com esse indice')
        else:
            raise Exception('A lista esta vazia')

    def remove(self, index):
        """Remove da lista o nodo com o indice especificado no argumento"""
        self.indexed = False
        current = self.search(index)
        if current == self.head == self.tail:
            self.head = self.tail = None
        elif current == self.tail:
            if not current.prevNode.next_10:
                current.prevNode.prev_1000 = current.prev_1000
                current.prevNode.prev_100 = current.prev_100
                current.prevNode.prev_10 = current.prev_10
                current.prev_1000.next_1000 = current.prevNode
                current.prev_100.next_100 = current.prevNode
                current.prev_10.next_10 = current.prevNode
            elif current.prevNode.next_10:
                if not current.prevNode.prev_1000:
                    current.prevNode.prev_1000 = current.prev_1000
                    current.prev_1000.next_1000 = current.prevNode
                if not current.prevNode.prev_100:
                    current.prevNode.prev_100 = current.prev_100
                    current.prev_100.next_100 = current.prevNode
                if not current.prevNode.prev_10:
                    current.prevNode.prev_10 = current.prev_10
                    current.prev_10.next_10 = current.prevNode
            self.tail = current.prevNode
            self.tail.nextNode = None
            self.tail.next_10 = None
            self.tail.next_100 = None
            self.tail.next_1000 = None
        elif current == self.head:
            if not current.nextNode.prev_10:
                current.nextNode.next_1000 = current.next_1000
                current.nextNode.next_100 = current.next_100
                current.nextNode.next_10 = current.next_10
                current.next_1000.prev_1000 = current.nextNode
                current.next_100.prev_100 = current.nextNode
                current.next_10.prev_10 = current.nextNode
            elif current.nextNode.prev_10:
                if not current.nextNode.next_1000:
                    current.nextNode.next_1000 = current.next_1000
                    current.next_1000.prev_1000 = current.nextNode
                if not current.nextNode.next_100:
                    current.nextNode.next_100 = current.next_100
                    current.next_100.prev_100 = current.nextNode
                if not current.nextNode.next_10:
                    current.nextNode.next_10 = current.next_10
                    current.next_10.prev_10 = current.nextNode
            self.head = current.nextNode
            self.head.prevNode = None
            self.head.prev_10 = None
            self.head.prev_100 = None
            self.head.prev_1000 = None
        else:
            if current.next_10:
                if not current.nextNode.prev_10:
                    current.nextNode.next_1000 = current.next_1000
                    current.nextNode.next_100 = current.next_100
                    current.nextNode.next_10 = current.next_10
                    current.next_1000.prev_1000 = current.nextNode
                    current.next_100.prev_100 = current.nextNode
                    current.next_10.prev_10 = current.nextNode
                elif current.nextNode.prev_10:
                    if not current.nextNode.next_1000:
                        current.nextNode.next_1000 = current.next_1000
                        current.next_1000.prev_1000 = current.nextNode
                    if not current.nextNode.next_100:
                        current.nextNode.next_100 = current.next_100
                        current.next_100.prev_100 = current.nextNode
                    if not current.nextNode.next_10:
                        current.nextNode.next_10 = current.next_10
                        current.next_10.prev_10 = current.nextNode
            current.nextNode.prevNode = current.prevNode
            current.prevNode.nextNode = current.nextNode

# utility functions - start #
    def iterator(self):
        current = self.head
        while current:
            next_1000 = current.next_1000.index if current.next_1000 else None
            next_100 = current.next_100.index if current.next_100 else None
            next_10 = current.next_10.index if current.next_10 else None
            prev_1000 = current.prev_1000.index if current.prev_1000 else None
            prev_100 = current.prev_100.index if current.prev_100 else None
            prev_10 = current.prev_10.index if current.prev_10 else None
            print('index:{}, next_10:{}, next_100:{}, next_1000:{}'.format(current.index, next_10, next_100, next_1000))
            print('          prev_10:{}, prev_100:{}, prev_1000:{}'.format(prev_10, prev_100, prev_1000))
            current = current.nextNode
# utility functions - end #

# tests
lista = IndexedList()
#lista.insert(10)
#lista.insert(8)
#lista.insert(11)
#lista.insert(12)
#lista.insert(15)
#lista.insert(14)
#lista.insert(13)
#lista.insert(7)
#lista.insert(18)
#lista.insert(9)
#lista.search(9)
#for i in range(1, 100):
#    lista.insert(i)

#print(lista.search(99).index)
lista.insert(1)
lista.insert(32)
lista.insert(312)
lista.insert(34)
lista.insert(95)
lista.insert(53)
lista.insert(94)
lista.insert(56)
lista.insert(78)
lista.insert(98)
lista.insert(45)
#lista.remove(91)
lista.remove(1)
lista.remove(34)

lista.iterator()

#print(lista.search(90).index)
