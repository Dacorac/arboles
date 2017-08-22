from Nodo import *
from Pila import Pila

def leerCadena():
	cadena = raw_input('Ingrese la cadena de caracteres a operar:')
	#listaCaracteres = []
	listaCaracteres = cadena.split(' ')
	return listaCaracteres

def crearArbol(lista, pila):
        for i in range(0,len(lista)):
                if lista[i] in "+-*/":
                        der = pila.sacarElemento()
                        izq = pila.sacarElemento()
                        nodoAux = Nodo(lista[i], izq, der)
                        pila.agregarElemento(nodoAux)
                else:
                        pila.agregarElemento(Nodo(int(lista[i]), None, None))
        return pila.sacarElemento()

def imprimirArbolPostfijo(arbol):
        if arbol != None:
                imprimirArbolPostfijo(arbol.izq)
                imprimirArbolPostfijo(arbol.der)
                print arbol.valor               


cadena = leerCadena()
pila = Pila()
nodo = crearArbol(cadena, pila)
print "impresion de Arbol:"
imprimirArbolPostfijo(nodo)
print "Resultado operacion: " , evaluar(nodo)
