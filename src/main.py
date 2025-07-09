import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from lexer import analizar_lexico
from yacc import analizar_sintactico, analizar_semantico

# ------------------ CONFIGURACIÓN VENTANA PRINCIPAL ------------------ #
ventana = tk.Tk()
ventana.title("Ruby Code Analyzer")
ventana.geometry("1000x800")
ventana.configure(bg="#0f0f0f")
ventana.resizable(True, True)

# ------------------ CANVAS CON SCROLL VERTICAL GLOBAL ------------------ #
canvas = tk.Canvas(ventana, bg="#0f0f0f")
scrollbar = tk.Scrollbar(ventana, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="#0f0f0f")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# ------------------ TÍTULO PRINCIPAL ------------------ #
tk.Label(scrollable_frame, text="Ruby Code Analyzer", font=("Helvetica", 32, "bold"), fg="#d0d0ff", bg="#0f0f0f").pack(pady=10)

# ------------------ CAMPO NOMBRE DE USUARIO ------------------ #
frame_usuario = tk.Frame(scrollable_frame, bg="#0f0f0f")
tk.Label(frame_usuario, text="Nombre de usuario:", font=("Helvetica", 12), fg="white", bg="#0f0f0f").pack(side=tk.LEFT, padx=5)
campo_usuario = tk.Entry(frame_usuario, width=30)
campo_usuario.pack(side=tk.LEFT)
frame_usuario.pack(pady=5)

# ------------------ ÁREA DE TEXTO PARA CÓDIGO ------------------ #
tk.Label(scrollable_frame, text="Código Ruby:", font=("Helvetica", 14), fg="white", bg="#0f0f0f").pack()
entrada_codigo = tk.Text(scrollable_frame, height=15, width=100, bg="#1e1e1e", fg="#dcdcdc", insertbackground="white")
entrada_codigo.pack(pady=10)

# ------------------ FUNCIONES DE BOTONES ------------------ #
def cargar_archivo():
    ruta = filedialog.askopenfilename(filetypes=[("Archivos Ruby", "*.rb")])
    if ruta:
        with open(ruta, "r", encoding="utf-8") as f:
            entrada_codigo.delete("1.0", tk.END)
            entrada_codigo.insert(tk.END, f.read())

def limpiar_campos():
    campo_usuario.delete(0, tk.END)
    entrada_codigo.delete("1.0", tk.END)
    for tabla in [tabla_tokens, tabla_sintactico, tabla_semantico]:
        for row in tabla.get_children():
            tabla.delete(row)

def analizar(tipo):
    codigo = entrada_codigo.get("1.0", tk.END).strip()
    if not codigo:
        messagebox.showwarning("Advertencia", "No hay código para analizar.")
        return
    usuario = campo_usuario.get().strip() or "Anonimo"
    archivo_temp = "codigo_temporal.rb"
    with open(archivo_temp, "w", encoding="utf-8") as f:
        f.write(codigo)
    try:
        if tipo == 'lexico':
            tokens = analizar_lexico(archivo_temp, usuario)
            mostrar_tokens(tokens)
        elif tipo == 'sintactico':
            errores = analizar_sintactico(archivo_temp, usuario)
            mostrar_errores(errores, tabla_sintactico)
        elif tipo == 'semantico':
            errores = analizar_semantico(archivo_temp, usuario)
            mostrar_errores(errores, tabla_semantico)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def mostrar_tokens(tokens):
    for row in tabla_tokens.get_children():
        tabla_tokens.delete(row)
    for tok in tokens:
        tabla_tokens.insert("", tk.END, values=tok)

def mostrar_errores(errores, tabla):
    for row in tabla.get_children():
        tabla.delete(row)
    for err in errores:
        tabla.insert("", tk.END, values=err)

# ------------------ BOTONES DE ANÁLISIS Y CONTROL ------------------ #
frame_botones = tk.Frame(scrollable_frame, bg="#0f0f0f")
btn_style = {"font": ("Helvetica", 12, "bold"), "bg": "#bbbbbb", "fg": "black", "width": 20, "height": 2}

tk.Button(frame_botones, text="📂 Cargar archivo", command=cargar_archivo, **btn_style).grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame_botones, text="🔍 Analizar léxico", command=lambda: analizar('lexico'), **btn_style).grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame_botones, text="🧩 Analizar sintáctico", command=lambda: analizar('sintactico'), **btn_style).grid(row=0, column=2, padx=5, pady=5)
tk.Button(frame_botones, text="🧠 Analizar semántico", command=lambda: analizar('semantico'), **btn_style).grid(row=0, column=3, padx=5, pady=5)
tk.Button(frame_botones, text="🗑️ Limpiar todo", command=limpiar_campos, **btn_style).grid(row=0, column=4, padx=5, pady=5)

frame_botones.pack(pady=10)

# ------------------ FUNCIONES PARA CREAR TABLAS ------------------ #
def crear_tabla(titulo, columnas):
    frame = tk.Frame(scrollable_frame, bg="#0f0f0f")
    tk.Label(frame, text=titulo, font=("Helvetica", 14, "bold"), fg="#d0d0ff", bg="#0f0f0f").pack()
    tabla = ttk.Treeview(frame, columns=columnas, show="headings", height=7)
    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, width=150)
    tabla.pack()
    frame.pack(pady=5)
    return tabla

# ------------------ ESTILO DE TABLAS ------------------ #
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", background="#1e1e1e", foreground="white", fieldbackground="#1e1e1e", font=("Helvetica", 11))
style.map("Treeview", background=[("selected", "#4a4a4a")])

# ------------------ TABLAS DE TOKENS, ERRORES SINTÁCTICOS Y SEMÁNTICOS ------------------ #
tabla_tokens = crear_tabla("📘 Tokens léxicos:", ["Tipo", "Valor", "Línea", "Posición"])
tabla_sintactico = crear_tabla("📙 Errores sintácticos:", ["Error", "Token", "Tipo", "Línea"])

tabla_semantico_columnas = ["Error", "Descripción"]
tabla_semantico = crear_tabla("📕 Errores semánticos:", tabla_semantico_columnas)
for col in tabla_semantico_columnas:
    tabla_semantico.column(col, width=300) 


# ------------------ EJECUCIÓN PRINCIPAL ------------------ #
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