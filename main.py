from cola import Cola
from pila import Pila

def prioridad(operador):
    if operador == "(":
        return 0
    elif operador == "+" or operador == "-":
        return 1
    elif operador == "/" or operador == "*":
        return 2
    else:
        return 3

def convertir_expresion():
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

    print("Resultado posfijo:", " ".join(arreglo))

def main():
    while True:
        print("\n" + "----------------------------")
        print("           MENÚ")
        print("----------------------------")
        print("1. Entrar (Convertir expresión a postfijo)")
        print("2. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            convertir_expresion()
        elif opcion == "2":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor digita 1 o 2.")

if __name__ == "__main__":
    main()