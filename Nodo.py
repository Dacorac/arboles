class Nodo():
	
	def __init__(self, valor, izq = None, der = None):
		self.valor = valor
		self.izq = izq
		self.der = der

def evaluar(arbol):
	if arbol.valor == '+':
		return evaluar(arbol.izq) + evaluar(arbol.der)

	if arbol.valor == '-':
		return evaluar(arbol.izq) - evaluar(arbol.der)
	
	if arbol.valor == '/':
		return evaluar(arbol.izq) / evaluar(arbol.der)

	if arbol.valor == '*':
		return evaluar(arbol.izq) * evaluar(arbol.der)

	return int(arbol.valor)
		