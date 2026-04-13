#Ejercicios de arrays, cadenas y funciones

#1. Algoritmo de ventas

#2. Crear menú de ventas
	#1 Ingresar artículos
	#2 Realizar venta
	#3 Mostrar artículos
	#4 Mostrar ventas

#2. Ingresar Articulos y sus precios  usando arrays (usar una función)

#3. Mostar los datos ingresados formato tabla (otra función)

#4. Crear una función Venta pidiendo  articulo, cantidad y guardar en un array de ventas

#5. Mostrar la venta

ventas=[]
inventario=[]

def ingresar_articulos():
    try:
        n=int(input("cuantos articulos deesea registrar?: "))
        for i in range(n):
            nombre=input("nombre del producto")
            precio=float(input("precio:"))
            producto={"nombre":nombre,"precio":precio}
            inventario.append(producto)
            print("Articulos reigstrados con exito")
    except ValueError:
        print("Error, ingrese valores validos")
        input("\npresione enter para continuar")

def mostrar_articulos():
    print(f"{'ID':<5} {'PRODUCTO':<10} {'PRECIO':10}")
    for i,p in enumerate(inventario):
        print(f"{i:<5} {p['nombre']:<10} {p['precio']:<10}")

def realizar_venta():
    try:
        mostrar_articulos()
        id_art=int(input("ingrese el id del articulo que desea: "))
        if 0<=id_art<len(inventario):
            cant=int(input("Ingrese la cantidad que desea: "))
            total=inventario[id_art]['precio']*cant
            registrar_venta={"articulo":inventario[id_art]['nombre'],"cantidad":cant,"total":total}
            ventas.append(registrar_venta)
            print("venta realizada con exito")
        else:
            print("Id no valido")
    except ValueError:
        print("Entrada no valida")
        input("\npresione enter para continuar")
def mostrar_ventas():
    print(f"{'Producto':<5} {'cantidad':<10} {'total':10}")
    for v in ventas:
        print(f"{v['articulo']:<5} {v['cantidad']:<10} {v['total']:<10}")

def menu():
    while True:
        print("SISTEMA DE VENTAS")
        print("1. ingresar articulo")
        print("2. mostrar articulos")
        print("3. realizar venta")
        print("4. mostrar ventas")
        print("5.salir")
        opcion=input("seleccione una opcion:")
        
        if opcion=="1":
            ingresar_articulos()
        elif opcion=="2":
            mostrar_articulos()
        elif opcion=="3":
            realizar_venta()
        elif opcion=="4":
            mostrar_ventas()    
        elif opcion=="5":
            break
        


if __name__=="__main__":
    menu()


