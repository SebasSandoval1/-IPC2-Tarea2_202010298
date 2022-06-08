

class Numero:
    def __init__(self,num):
        self.num = num
        self.siguiente = None
        self.anterior = None

class ListaDoble:
    def __init__(self):
        self.head = None
        self.last = None
        self.tamanio = 0

    def add(self,num):
        nuevo = Numero(num)
        if self.tamanio == 0:
            self.head = nuevo
            self.last = nuevo
            self.tamanio =+1
        else:
            self.last = self.head
            self.last.anterior = nuevo
            nuevo.siguiente = self.last
            self.head = nuevo




    def print(self):
        aux = self.head
        while aux != None:
            print(aux.num)
            aux = aux.siguiente

    def buscar(self, buscado):
        aux = self.head
        while aux != None:
            if aux.num == buscado:
                if aux.siguiente == None:
                    print("Anterior: " + " " + ", Actual: " + str(aux.num) + ", Siguiente: " + str(
                        aux.anterior.num))
                elif aux.anterior == None:
                    print("Anterior: " + str(aux.siguiente.num) + ", Actual: " + str(aux.num) + ", Siguiente: " + " ")
                elif aux.anterior.num != None and aux.siguiente.num != None:
                    print("Anterior: "+ str(aux.siguiente.num) +", Actual: "+str(aux.num)+ ", Siguiente: "+ str(aux.anterior.num))
            aux = aux.siguiente

if __name__ == "__main__":
    ListaDoble = ListaDoble()

    ListaDoble.add(1)
    ListaDoble.add(2)
    ListaDoble.add(4)
    ListaDoble.add(5)
    ListaDoble.add(7)
    ListaDoble.add(9)
    ListaDoble.add(15)
    print("Listado de Numeros:")
    ListaDoble.print()
    buscado = int(input("Seleccione Numero: "))
    ListaDoble.buscar(buscado)




