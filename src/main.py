import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from lexer import analizar_lexico
from yacc import analizar_sintactico, analizar_semantico

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
        errores_sintacticos = analizar_sintactico(archivo_temp, usuario)
        errores_semanticos = analizar_semantico(archivo_temp, usuario)

        mostrar_tokens(tokens)
        mostrar_errores_sintac(errores_sintacticos, tabla_sintactico)
        mostrar_errores_semant(errores_semanticos, tabla_semantico)

    except Exception as e:
        messagebox.showerror("Error", str(e))

def mostrar_tokens(tokens):
    for row in tabla_tokens.get_children():
        tabla_tokens.delete(row)

    for tok in tokens:
        tipo, valor, linea, pos = tok
        tabla_tokens.insert("", tk.END, values=(tipo, valor, linea, pos))

def mostrar_errores_sintac(errores, tabla):
    for row in tabla.get_children():
        tabla.delete(row)
    for err in errores:
        error, token, tipo, linea = err
        tabla.insert("", tk.END, values=(error, token, tipo, linea))

def mostrar_errores_semant(errores, tabla):
    for row in tabla.get_children():
        tabla.delete(row)
    for err in errores:
        tipo, descripcion = err
        tabla.insert("", tk.END, values=(tipo, descripcion))

# Crear ventana
ventana = tk.Tk()
ventana.title("Ruby Code Analyzer")
ventana.geometry("1000x1000")

# Campo usuario
tk.Label(ventana, text="Nombre de usuario:").pack(pady=5)
campo_usuario = tk.Entry(ventana, width=30)
campo_usuario.pack()

# Área de texto para código
tk.Label(ventana, text="Código Ruby:").pack()
entrada_codigo = tk.Text(ventana, height=5, width=100)
entrada_codigo.pack(pady=5)

# Botones
frame_botones = tk.Frame(ventana)
frame_botones.pack()

tk.Button(frame_botones, text="📂 Cargar archivo", command=cargar_archivo).pack(side=tk.LEFT, padx=10)
tk.Button(frame_botones, text="🧠 Analizar código", command=analizar).pack(side=tk.LEFT, padx=10)


# Tabla de tokens
tk.Label(ventana, text="📘 Tokens léxicos:").pack(pady=5)
columnas = ("Tipo", "Valor", "Línea", "Posición")
tabla_tokens = ttk.Treeview(ventana, columns=columnas, show="headings", height=5)
for col in columnas:
    tabla_tokens.heading(col, text=col)
    tabla_tokens.column(col, width=150)
tabla_tokens.pack(pady=5)

# Tabla de errores sintácticos
tk.Label(ventana, text="📙 Errores sintácticos:").pack(pady=5)
cols_sintactico = ("Error", "Token", "Tipo", "Línea")
tabla_sintactico = ttk.Treeview(ventana, columns=cols_sintactico, show="headings", height=5)
for col in cols_sintactico:
    tabla_sintactico.heading(col, text=col)
    tabla_sintactico.column(col, width=150)
tabla_sintactico.pack(pady=5)

# Tabla de errores semánticos
tk.Label(ventana, text="📕 Errores semánticos:").pack(pady=5)
cols_semantico = ("Error", "Descripción")
tabla_semantico = ttk.Treeview(ventana, columns=cols_semantico, show="headings", height=5)
for col in cols_semantico:
    tabla_semantico.heading(col, text=col)
    tabla_semantico.column(col, width=300)
tabla_semantico.pack(pady=5)

ventana.mainloop()


#PRUEBA PARA EJECUTAR ANALISIS LEXICO CON LA RUTA
nombre_usuario = "ggpachec"  # cambiar por cada usuario Git
archivo_prueba = "../src/algoritmos/algoritmo_genesis.rb"  # cambiar por el archivo de cada uno

tokenss = analizar_lexico(archivo_prueba, nombre_usuario)

# Imprime tokens en consola
print("\n📌 Lista de tokens encontrados:")
for t in tokenss:
    tipo, valor, linea, pos = t
    print(f"{tipo}\t{valor}\tLínea {linea}\tPos {pos}")
