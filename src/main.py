import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from lexer import analizar_lexico

def cargar_archivo():
    ruta = filedialog.askopenfilename(filetypes=[("Archivos Ruby", "*.rb")])
    if ruta:
        with open(ruta, "r", encoding="utf-8") as f:
            contenido = f.read()
            entrada_codigo.delete("1.0", tk.END)
            entrada_codigo.insert(tk.END, contenido)

def analizar():
    codigo = entrada_codigo.get("1.0", tk.END).strip()
    if not codigo:
        messagebox.showwarning("Advertencia", "No hay código para analizar.")
        return

    usuario = campo_usuario.get().strip() or "Anonimo"

    # Guardar código temporal en archivo para compatibilidad con tu lexer
    archivo_temp = "codigo_temporal.rb"
    with open(archivo_temp, "w", encoding="utf-8") as f:
        f.write(codigo)

    try:
        tokens = analizar_lexico(archivo_temp, usuario)
        mostrar_tokens(tokens)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def mostrar_tokens(tokens):
    for row in tabla_tokens.get_children():
        tabla_tokens.delete(row)

    for tok in tokens:
        tipo, valor, linea, pos = tok
        tabla_tokens.insert("", tk.END, values=(tipo, valor, linea, pos))

# Crear ventana
ventana = tk.Tk()
ventana.title("Analizador Léxico Ruby")
ventana.geometry("900x600")

# Campo usuario
tk.Label(ventana, text="Nombre de usuario:").pack(pady=5)
campo_usuario = tk.Entry(ventana, width=30)
campo_usuario.pack()

# Área de texto para código
tk.Label(ventana, text="Código Ruby:").pack()
entrada_codigo = tk.Text(ventana, height=15, width=100)
entrada_codigo.pack(pady=5)

# Botones
frame_botones = tk.Frame(ventana)
frame_botones.pack()

tk.Button(frame_botones, text="📂 Cargar archivo", command=cargar_archivo).pack(side=tk.LEFT, padx=10)
tk.Button(frame_botones, text="🧠 Analizar léxico", command=analizar).pack(side=tk.LEFT, padx=10)

# Tabla de tokens
tk.Label(ventana, text="Tokens léxicos:").pack(pady=5)
columnas = ("Tipo", "Valor", "Línea", "Posición")
tabla_tokens = ttk.Treeview(ventana, columns=columnas, show="headings", height=10)

for col in columnas:
    tabla_tokens.heading(col, text=col)
    tabla_tokens.column(col, width=150)

tabla_tokens.pack(pady=10)

# Ejecutar la GUI
ventana.mainloop()


#PRUEBA PARA EJECUTAR ANALISIS LEXICO CON
nombre_usuario = "ggpachec"  # cambiar por cada usuario Git
archivo_prueba = "../src/algoritmos/algoritmo_genesis.rb"  # cambiar por el archivo de cada uno

tokenss = analizar_lexico(archivo_prueba, nombre_usuario)

# Imprime tokens en consola
print("\n📌 Lista de tokens encontrados:")
for t in tokenss:
    tipo, valor, linea, pos = t
    print(f"{tipo}\t{valor}\tLínea {linea}\tPos {pos}")
