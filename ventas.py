import os

# "Arrays" globales para almacenar la información
articulos = []
precios = []
ventas = []

def ingresar_articulos():
    print("\n--- Registro de Artículos ---")
    n = int(input("¿Cuántos artículos desea ingresar?: "))
    for i in range(n):
        nombre = input(f"Nombre del artículo {i+1}: ")
        precio = float(input(f"Precio de {nombre}: "))
        articulos.append(nombre)
        precios.append(precio)
    print("Artículos registrados con éxito.")

def mostrar_articulos():
    print("\n--- Inventario de Artículos ---")
    print(f"{'ID':<5} {'Artículo':<20} {'Precio':<10}")
    print("-" * 35)
    for i in range(len(articulos)):
        print(f"{i:<5} {articulos[i]:<20} ${precios[i]:<10.2f}")

def realizar_venta():
    if not articulos:
        print("\nError: No hay artículos registrados para vender.")
        return

    mostrar_articulos()
    try:
        id_art = int(input("\nIngrese el ID del artículo a vender: "))
        if 0 <= id_art < len(articulos):
            cant = int(input(f"¿Cuántas unidades de '{articulos[id_art]}'?: "))
            total = precios[id_art] * cant
            
            # Guardamos la venta como un string formateado o una pequeña lista
            registro = f"{articulos[id_art]} | Cant: {cant} | Total: ${total:.2f}"
            ventas.append(registro)
            print(f"Venta realizada: ${total:.2f}")
        else:
            print("ID no válido.")
    except ValueError:
        print("Error: Ingrese valores numéricos válidos.")

def mostrar_ventas():
    print("\n--- Historial de Ventas ---")
    if not ventas:
        print("No se han realizado ventas aún.")
    else:
        for v in ventas:
            print(v)

def menu():
    while True:
        print("\n--- MENÚ DE VENTAS ---")
        print("1. Ingresar artículos")
        print("2. Realizar venta")
        print("3. Mostrar artículos (Tabla)")
        print("4. Mostrar ventas")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ingresar_articulos()
        elif opcion == "2":
            realizar_venta()
        elif opcion == "3":
            mostrar_articulos()
        elif opcion == "4":
            mostrar_ventas()
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()
