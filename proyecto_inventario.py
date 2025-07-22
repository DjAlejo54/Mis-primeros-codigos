import sqlite3
from colorama import init, Fore, Style

# Inicializar colorama
init(autoreset=True)

# Conectar a la base de datos (se crea si no existe)
conn = sqlite3.connect("inventario.db")
cursor = conn.cursor()

# Crear tabla si no existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT,
    cantidad INTEGER NOT NULL,
    precio REAL NOT NULL,
    categoria TEXT
)
""")
conn.commit()


# Funciones

def mostrar_menu():
    print(Fore.CYAN + "\n--- MENÚ PRINCIPAL ---")
    print("1. Registrar nuevo producto")
    print("2. Ver todos los productos")
    print("3. Actualizar producto por ID")
    print("4. Eliminar producto por ID")
    print("5. Buscar producto por ID")
    print("6. Reporte de stock bajo")
    print("7. Salir")


def registrar_producto():
    print(Fore.YELLOW + "\n--- Registrar producto ---")
    nombre = input("Nombre: ").strip()
    descripcion = input("Descripción: ").strip()
    categoria = input("Categoría: ").strip()

    while True:
        cantidad = input("Cantidad: ").strip()
        if cantidad.isdigit():
            cantidad = int(cantidad)
            break
        else:
            print(Fore.RED + "Cantidad inválida. Ingresá un número entero.")

    while True:
        precio = input("Precio: ").replace(",", ".").strip()
        try:
            precio = float(precio)
            break
        except ValueError:
            print(Fore.RED + "Precio inválido. Ingresá un número.")

    cursor.execute("INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria) VALUES (?, ?, ?, ?, ?)",
                   (nombre, descripcion, cantidad, precio, categoria))
    conn.commit()
    print(Fore.GREEN + "✅ Producto registrado correctamente.")


def ver_productos():
    print(Fore.YELLOW + "\n--- Lista de productos ---")
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    if productos:
        for prod in productos:
            print(f"{Fore.CYAN}ID: {prod[0]} | Nombre: {prod[1]} | Cantidad: {prod[3]} | Precio: ${prod[4]:.2f} | Categoría: {prod[5]}")
            print(f"{Style.DIM}Descripción: {prod[2]}")
            print("-" * 50)
    else:
        print(Fore.RED + "No hay productos registrados.")


def actualizar_producto():
    print(Fore.YELLOW + "\n--- Actualizar producto ---")
    prod_id = input("ID del producto a actualizar: ").strip()
    if not prod_id.isdigit():
        print(Fore.RED + "ID inválido.")
        return

    cursor.execute("SELECT * FROM productos WHERE id = ?", (prod_id,))
    producto = cursor.fetchone()
    if not producto:
        print(Fore.RED + "No se encontró un producto con ese ID.")
        return

    nuevo_nombre = input(f"Nuevo nombre [{producto[1]}]: ").strip() or producto[1]
    nueva_descripcion = input(f"Nueva descripción [{producto[2]}]: ").strip() or producto[2]
    nueva_categoria = input(f"Nueva categoría [{producto[5]}]: ").strip() or producto[5]

    while True:
        nueva_cantidad = input(f"Nueva cantidad [{producto[3]}]: ").strip()
        if nueva_cantidad == "":
            nueva_cantidad = producto[3]
            break
        elif nueva_cantidad.isdigit():
            nueva_cantidad = int(nueva_cantidad)
            break
        else:
            print(Fore.RED + "Cantidad inválida.")

    while True:
        nuevo_precio = input(f"Nuevo precio [{producto[4]}]: ").strip().replace(",", ".")
        if nuevo_precio == "":
            nuevo_precio = producto[4]
            break
        try:
            nuevo_precio = float(nuevo_precio)
            break
        except ValueError:
            print(Fore.RED + "Precio inválido.")

    cursor.execute("""
        UPDATE productos 
        SET nombre=?, descripcion=?, cantidad=?, precio=?, categoria=?
        WHERE id=?""",
        (nuevo_nombre, nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_categoria, prod_id))
    conn.commit()
    print(Fore.GREEN + "✅ Producto actualizado correctamente.")


def eliminar_producto():
    print(Fore.YELLOW + "\n--- Eliminar producto ---")
    prod_id = input("ID del producto a eliminar: ").strip()
    if not prod_id.isdigit():
        print(Fore.RED + "ID inválido.")
        return

    cursor.execute("SELECT * FROM productos WHERE id = ?", (prod_id,))
    if not cursor.fetchone():
        print(Fore.RED + "No se encontró un producto con ese ID.")
        return

    cursor.execute("DELETE FROM productos WHERE id = ?", (prod_id,))
    conn.commit()
    print(Fore.GREEN + "✅ Producto eliminado.")


def buscar_producto():
    print(Fore.YELLOW + "\n--- Buscar producto ---")
    prod_id = input("ID del producto a buscar: ").strip()
    if not prod_id.isdigit():
        print(Fore.RED + "ID inválido.")
        return

    cursor.execute("SELECT * FROM productos WHERE id = ?", (prod_id,))
    prod = cursor.fetchone()
    if prod:
        print(f"{Fore.CYAN}ID: {prod[0]} | Nombre: {prod[1]} | Cantidad: {prod[3]} | Precio: ${prod[4]:.2f} | Categoría: {prod[5]}")
        print(f"{Style.DIM}Descripción: {prod[2]}")
    else:
        print(Fore.RED + "No se encontró un producto con ese ID.")


def reporte_stock_bajo():
    print(Fore.YELLOW + "\n--- Reporte de stock bajo ---")
    while True:
        limite = input("Mostrar productos con cantidad menor o igual a: ").strip()
        if limite.isdigit():
            limite = int(limite)
            break
        else:
            print(Fore.RED + "Límite inválido.")

    cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (limite,))
    productos = cursor.fetchall()
    if productos:
        print(Fore.LIGHTMAGENTA_EX + "\nProductos con bajo stock:")
        for prod in productos:
            print(f"ID: {prod[0]} | {prod[1]} - Cantidad: {prod[3]}")
    else:
        print(Fore.GREEN + "No hay productos con stock bajo.")


# Bucle principal

def main():
    while True:
        mostrar_menu()
        opcion = input(Fore.BLUE + "Elegí una opción: ").strip()
        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            ver_productos()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            buscar_producto()
        elif opcion == "6":
            reporte_stock_bajo()
        elif opcion == "7":
            print(Fore.CYAN + "¡Hasta luego!")
            break
        else:
            print(Fore.RED + "Opción inválida. Elegí del 1 al 7.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
    conn.close()
