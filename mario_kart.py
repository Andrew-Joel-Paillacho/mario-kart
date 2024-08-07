# Definimos la función de ordenamiento por inserción en orden descendente
def ordenamiento_insercion_descendente(lista):
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1
        while j >= 0 and key > lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key
    return lista

# Función principal para gestionar el ingreso de monedas y determinar el ganador
def modulo_mario_kart():
    competidores = ['Competidor 1', 'Competidor 2', 'Competidor 3']
    monedas_recogidas = []

    print("\n======================================================")
    print("\n--------- MODULO DE RANKING DE MONEDAS ----------\n")
    
    # Ingresamos las monedas recogidas por cada competidor
    for competidor in competidores:
        while True:
            try:
                monedas = int(input(f"Ingrese las monedas recogidas por {competidor}: "))
                monedas_recogidas.append(monedas)
                break
            except ValueError:
                print("Por favor, ingrese un número entero válido.")

    # Determinamos el ganador
    max_monedas = max(monedas_recogidas)
    ganador_index = monedas_recogidas.index(max_monedas)
    ganador = competidores[ganador_index]

    print("\n======================================================")
    print(f"\nEl ganador es: {ganador} con {max_monedas} monedas.")
    print("\n======================================================")

    # Ordenamos las monedas utilizando el algoritmo de ordenamiento por inserción en orden descendente
    monedas_ordenadas = ordenamiento_insercion_descendente(monedas_recogidas.copy())

    print("\nMonedas recogidas ordenadas:")
    for i, monedas in enumerate(monedas_ordenadas, 1):
        print(f"\t[{i}] {monedas} monedas")
        
    print("\n======================================================")

# Ejecutamos el módulo
if __name__ == "__main__":
    modulo_mario_kart()
