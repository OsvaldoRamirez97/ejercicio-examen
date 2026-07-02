ventas = [
{"vendedor": "Ana", "producto": "Mouse", "cantidad": 3, "precio": 1500},
{"vendedor": "Juan", "producto": "Teclado", "cantidad": 2, "precio": 3000},
{"vendedor": "Ana", "producto": "Monitor", "cantidad": 1, "precio": 25000},
{"vendedor": "Luis", "producto": "Mouse", "cantidad": 4, "precio": 1500}
]

#paramentro formal es el que recibe la funcion que se reemplaza cuando es invocada
def mostrar_mayor_venta(lista: list) -> None:
    mayor_venta = []
    venta_mas_alta = lista[0]['cantidad'] * lista[0]['precio']
    
    for i in range(1, len(lista)):
        venta_actual = lista[i]['cantidad'] * lista[i]['precio'] 

        if venta_actual > venta_mas_alta:
            venta_mas_alta = venta_actual
            mayor_venta = lista[i]
    
    return mayor_venta

#Invocacion
mostrar_mayor_venta(ventas)
#paramentro acutal el que recibe cuando es invocada