print(" ")
print("Alvaro Campechano 3W")
print(" ")
def main():
    """
    Función principal que solicita un número entero al usuario
    y verifica si es divisible por 7 y mayor a 40.
    """
    # Solicitar al usuario un número entero
    try:
        numero = int(input("Ingresa un número entero: "))
        
        # Verificar si el número es mayor a 40 y divisible por 7
        if numero > 40:
            if numero % 7 == 0:
                print(f"El número {numero} es mayor a 40 y es divisible por 7.")
            else:
                print(f"El número {numero} es mayor a 40, pero no es divisible por 7.")
        else:
            print(f"El número {numero} no es mayor a 40.")
    
    except ValueError:
        print("Entrada no válida. Asegúrate de ingresar un número entero.")

# Ejecutar la función principal si el script es ejecutado directamente
if __name__ == "__main__":
    main()
