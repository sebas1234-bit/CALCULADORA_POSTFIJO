from cola import Cola
from pila import Pila
def main():
    numero = input("Expresión para convertir a postfijo: ")
    numero_junto = numero.replace(" ", "")
    vector = list(numero_junto)
    numero_para_cola = Cola()
    numero_para_pila = Pila()
    numero_actual = ""
    for elemento in vector:
        if elemento.isdigit():
            numero_actual += elemento          
            continue

        if numero_actual != "":
            numero_para_cola.add(numero_actual)
            numero_actual = ""  

        if elemento == "(":
            numero_para_pila.push(elemento)
        elif elemento == ")":
            while numero_para_pila.peek() != "(":
                if numero_para_pila.peek() == None:
                    print("Error: paréntesis desbalanceados")
                    return
                numero_para_cola.add(numero_para_pila.pop())
            numero_para_pila.pop() 
        else:
            while True:
                if numero_para_pila.peek() == None:
                    numero_para_pila.push(elemento)
                    break
                elif prioridad(numero_para_pila.peek()) < prioridad(elemento):
                    numero_para_pila.push(elemento)
                    break
                else:
                    numero_para_cola.add(numero_para_pila.pop())

    if numero_actual != "":
        numero_para_cola.add(numero_actual)
    while numero_para_pila.peek() != None:
        if numero_para_pila.peek() == "(":
            print("Error: paréntesis desbalanceados")
            return
        numero_para_cola.add(numero_para_pila.pop())

    arreglo = []
    while numero_para_cola.peek() != None:
        arreglo.append(numero_para_cola.poll())
    print(" ".join(arreglo))

    #numero_para_cola.mostrar()   
    #print()       
    #numero_para_pila.mostrar()
    
def prioridad(operador):
    if operador == "(":
        return 0
    elif operador == "+" or operador == "-":
        return 1
    elif operador == "/" or operador == "*":
        return 2
    else:
        return 3


if __name__ == "__main__":
    main()