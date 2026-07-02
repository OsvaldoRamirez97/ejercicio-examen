ventas = [
{"vendedor": "Ana", "producto": "Mouse", "cantidad": 3, "precio": 1500},
{"vendedor": "Juan", "producto": "Teclado", "cantidad": 2, "precio": 3000},
{"vendedor": "Ana", "producto": "Monitor", "cantidad": 1, "precio": 25000},
{"vendedor": "Luis", "producto": "Mouse", "cantidad": 4, "precio": 1500}
]

# Realizar una funcion que reciba por parametro una lista de diccionarios como la de arriba y su funcionalidad sea retornar el diccionario que represente al mayor precio de venta sobe todos.
# Nota: Indicar como comentario en el programa los parámetros formales, los parámetros actuales y la invocación. Documentar la función

def mostrar_mayor_venta(lista: list) -> None:
    mayor_venta = []
    venta_mas_alta = lista[0]['cantidad'] * lista[0]['precio']
    
    for i in range(1, len(lista)):
        venta_actual = lista[i]['cantidad'] * lista[i]['cantidad'] 
        if venta_actual > venta_mas_alta:
            venta_mas_alta = venta_actual
            mayor_venta = lista[i]
    
    return mayor_venta

print(mostrar_mayor_venta(ventas))