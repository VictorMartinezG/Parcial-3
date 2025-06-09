# Bubble Sort: ordena una lista de precios de menor a mayor

def bubble_sort(prices):
    n = len(prices)  # Obtenemos la cantidad de elementos en la lista

    # Recorremos todos los elementos
    for i in range(n):
        # En cada pasada, el mayor se "va al final", así que recorremos menos cada vez
        for j in range(0, n - i - 1):
            # Si el precio actual es mayor que el siguiente, los intercambiamos
            if prices[j] > prices[j + 1]:
                prices[j], prices[j + 1] = prices[j + 1], prices[j]  # Intercambio

# Caso real: precios en una tienda
precios = [19.99, 4.50, 15.00, 3.25, 9.99]
bubble_sort(precios)  # Ordenamos los precios
print("Precios ordenados (Bubble Sort):", precios)

print("-" * 50)  # Imprime una línea con 50 guiones como separador

# Insertion Sort: ordena una lista de edades de menor a mayor

def insertion_sort(ages):
    # Recorremos la lista desde el segundo elemento
    for i in range(1, len(ages)):
        key = ages[i]  # Tomamos la edad actual como referencia
        j = i - 1  # Comparamos con el anterior

        # Mientras haya edades mayores a la actual, las movemos a la derecha
        while j >= 0 and key < ages[j]:
            ages[j + 1] = ages[j]  # Movemos la edad hacia la derecha
            j -= 1  # Seguimos comparando hacia la izquierda

        # Colocamos la edad actual en la posición correcta
        ages[j + 1] = key

# Caso real: edades de personas en una lista
edades = [34, 21, 45, 18, 30]
insertion_sort(edades)  # Ordenamos las edades
print("Edades ordenadas (Insertion Sort):", edades)

print("-" * 50)  # Imprime una línea con 50 guiones como separador

# Selection Sort: ordena una lista de calificaciones de menor a mayor

def selection_sort(grades):
    n = len(grades)  # Cantidad de elementos en la lista

    # Recorremos cada posición de la lista
    for i in range(n):
        min_index = i  # Suponemos que el mínimo está en la posición i

        # Recorremos el resto de la lista para encontrar el mínimo real
        for j in range(i + 1, n):
            if grades[j] < grades[min_index]:
                min_index = j  # Actualizamos el índice del nuevo mínimo

        # Intercambiamos el valor actual con el mínimo encontrado
        grades[i], grades[min_index] = grades[min_index], grades[i]

# Caso real: calificaciones de estudiantes
calificaciones = [85, 92, 76, 98, 88]
selection_sort(calificaciones)  # Ordenamos las calificaciones
print("Calificaciones ordenadas (Selection Sort):", calificaciones)

print("-" * 50)  # Imprime una línea con 50 guiones como separador

# Merge Sort: ordena tiempos de corredores (en segundos) de menor a mayor
# Usa el método de "divide y vencerás": divide la lista en partes más pequeñas y luego las une ordenadas

def merge_sort(times):
    # Si la lista tiene más de un elemento, la dividimos
    if len(times) > 1:
        mid = len(times) // 2  # Punto medio
        left_half = times[:mid]  # Mitad izquierda
        right_half = times[mid:]  # Mitad derecha

        # Llamadas recursivas para ordenar cada mitad
        merge_sort(left_half)
        merge_sort(right_half)

        # Unimos las mitades ya ordenadas
        i = j = k = 0  # i y j recorren las mitades, k la lista original

        # Comparamos y mezclamos elementos de ambas mitades
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                times[k] = left_half[i]  # Insertamos el menor en la lista original
                i += 1
            else:
                times[k] = right_half[j]
                j += 1
            k += 1

        # Si quedan elementos en la mitad izquierda, los agregamos
        while i < len(left_half):
            times[k] = left_half[i]
            i += 1
            k += 1

        # Si quedan elementos en la mitad derecha, los agregamos
        while j < len(right_half):
            times[k] = right_half[j]
            j += 1
            k += 1

# Caso real: tiempos en segundos de una carrera
tiempos = [58.3, 62.1, 55.0, 61.2, 59.7]
merge_sort(tiempos)
print("Tiempos ordenados (Merge Sort):", tiempos)

print("-" * 50)  # Imprime una línea con 50 guiones como separador

# Quick Sort: ordena número de visitas de páginas web de menor a mayor
# Usa un "pivote" y divide la lista en menores y mayores que ese pivote

def quick_sort(visits):
    # Si la lista tiene 1 o 0 elementos, ya está ordenada
    if len(visits) <= 1:
        return visits

    pivot = visits[0]  # Elegimos el primer elemento como pivote

    # Creamos listas con elementos menores, iguales y mayores al pivote
    menores = [x for x in visits[1:] if x < pivot]
    iguales = [x for x in visits if x == pivot]
    mayores = [x for x in visits[1:] if x > pivot]

    # Ordenamos recursivamente y concatenamos el resultado
    return quick_sort(menores) + iguales + quick_sort(mayores)

# Caso real: número de visitas diarias a una web
visitas = [300, 120, 500, 200, 400]
visitas_ordenadas = quick_sort(visitas)
print("Visitas ordenadas (Quick Sort):", visitas_ordenadas)

print("-" * 50)  # Imprime una línea con 50 guiones como separador

# Heap Sort: ordena ganancias de sucursales usando un "heap" (montículo)
# Un heap permite encontrar el valor más grande o más pequeño rápidamente

def heapify(arr, n, i):
    largest = i  # Suponemos que el mayor está en la raíz
    left = 2 * i + 1  # Hijo izquierdo
    right = 2 * i + 2  # Hijo derecho

    # Si el hijo izquierdo es mayor que la raíz
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Si el hijo derecho es mayor que el mayor actual
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Si el mayor no es la raíz, intercambiamos y aplicamos heapify de nuevo
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Intercambio
        heapify(arr, n, largest)  # Reorganizamos el subárbol afectado

def heap_sort(arr):
    n = len(arr)

    # Construimos un max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extraemos elementos del heap uno por uno
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Movemos el mayor al final
        heapify(arr, i, 0)  # Restauramos el heap

# Caso real: ganancias mensuales en miles de pesos
ganancias = [120, 80, 150, 90, 110]
heap_sort(ganancias)
print("Ganancias ordenadas (Heap Sort):", ganancias)
