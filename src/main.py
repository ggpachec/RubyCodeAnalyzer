import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from lexer import analizar_lexico
from yacc import analizar_sintactico, analizar_semantico

# ===== Clase auxiliar para mostrar números de línea =====
class TextLineNumbers(tk.Canvas):
    def __init__(self, master, text_widget, **kwargs):
        super().__init__(master, **kwargs)
        self.text_widget = text_widget
        self.text_widget.bind("<<Change>>", self._on_change)
        self.text_widget.bind("<Configure>", self._on_change)
        self.text_widget.bind("<KeyRelease>", self._on_change)
        self._on_change()

    def _on_change(self, event=None):
        self.delete("all")
        i = self.text_widget.index("@0,0")
        while True:
            dline = self.text_widget.dlineinfo(i)
            if dline is None:
                break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.create_text(5, y, anchor="nw", text=linenum, font=self.text_widget["font"], fill="#888")
            i = self.text_widget.index(f"{i}+1line")

def scroll_con_mouse(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

def on_change(event):
    entrada_codigo.edit_modified(0)
    linea_numeros._on_change()


# ------------------ CONFIGURACIÓN VENTANA PRINCIPAL ------------------ #
ventana = tk.Tk()
ventana.title("Ruby Code Analyzer")
ventana.configure(bg="#0f0f0f")
ventana.state('zoomed')
ventana.resizable(True, True)

# ------------------ TÍTULO PRINCIPAL ------------------ #
frame_titulo = tk.Frame(ventana, bg="#0f0f0f")
frame_titulo.pack(fill="x")

tk.Label(frame_titulo, text="Ruby Code Analyzer", font=("Helvetica", 32, "bold"),
         fg="#d0d0ff", bg="#0f0f0f").pack(pady=10)


# ------------------ CANVAS CON SCROLL VERTICAL GLOBAL ------------------ #
canvas = tk.Canvas(ventana, bg="#0f0f0f", highlightthickness=0)
scrollbar = tk.Scrollbar(ventana, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

scrollable_frame = tk.Frame(canvas, bg="#0f0f0f")

# Empaquetar contenido en el centro superior
canvas_window = canvas.create_window((0, 0), window=scrollable_frame, anchor="n", width=canvas.winfo_width())

# Asegura que el scroll funcione y el contenido se mantenga centrado
def resize_canvas(event):
    canvas.itemconfig(canvas_window, width=event.width)

scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
scrollable_frame.bind_all("<MouseWheel>", scroll_con_mouse)
canvas.bind("<Configure>", resize_canvas)

# ------------------ CAMPO NOMBRE DE USUARIO ------------------ #
frame_usuario = tk.Frame(scrollable_frame, bg="#0f0f0f")
tk.Label(frame_usuario, text="Username:", font=("Helvetica", 12), fg="white", bg="#0f0f0f").pack(side=tk.LEFT, padx=5)
campo_usuario = tk.Entry(frame_usuario, width=30)
campo_usuario.pack(side=tk.LEFT)
frame_usuario.pack(pady=5)

# ------------------ ÁREA DE TEXTO PARA CÓDIGO ------------------ #
tk.Label(scrollable_frame, text="Ruby Code:", font=("Helvetica", 14), fg="white", bg="#0f0f0f").pack()

editor_frame = tk.Frame(scrollable_frame, bg="#0f0f0f")
editor_frame.pack(fill=tk.BOTH, expand=True, pady=10)

entrada_codigo = tk.Text(editor_frame, height=20, width=100, bg="#1e1e1e", fg="#dcdcdc",
                         insertbackground="white", font=("Courier New", 11))
entrada_codigo.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

linea_numeros = TextLineNumbers(editor_frame, entrada_codigo, width=30, bg="#0f0f0f")
linea_numeros.pack(side=tk.LEFT, fill=tk.Y)

entrada_codigo.bind("<<Modified>>", on_change)


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
        messagebox.showwarning("Warning", "No code to parse.")
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

tk.Button(frame_botones, text="📂 Upload file", command=cargar_archivo, **btn_style).grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame_botones, text="🔍 Lexical Analysis", command=lambda: analizar('lexico'), **btn_style).grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame_botones, text="🧩 Syntactic Analysis", command=lambda: analizar('sintactico'), **btn_style).grid(row=0, column=2, padx=5, pady=5)
tk.Button(frame_botones, text="🧠 Semantic Analysis", command=lambda: analizar('semantico'), **btn_style).grid(row=0, column=3, padx=5, pady=5)
tk.Button(frame_botones, text="🗑️ Clean", command=limpiar_campos, **btn_style).grid(row=0, column=4, padx=5, pady=5)

frame_botones.pack(pady=10)

# ------------------ FUNCIONES PARA CREAR TABLAS ------------------ #
def crear_tabla(titulo, columnas):
    frame = tk.Frame(scrollable_frame, bg="#0f0f0f")
    tk.Label(frame, text=titulo, font=("Helvetica", 14, "bold"), fg="#d0d0ff", bg="#0f0f0f").pack()

    contenedor = tk.Frame(frame)
    contenedor.pack()


    scrollbar = tk.Scrollbar(contenedor, orient="vertical")
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    tabla = ttk.Treeview(contenedor, columns=columnas, show="headings", height=7, yscrollcommand=scrollbar.set)
    tabla.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, width=150)
    scrollbar.config(command=tabla.yview)

    # Vincular el scroll del mouse
    def scroll_tabla(event, tree):
        tree.yview_scroll(int(-1 * (event.delta / 120)), "units")

    tabla.bind("<Enter>", lambda e: tabla.bind("<MouseWheel>", lambda ev: scroll_tabla(ev, tabla)))
    tabla.bind("<Leave>", lambda e: tabla.unbind("<MouseWheel>"))

    frame.pack(pady=5, fill="x")
    return tabla

# ------------------ ESTILO DE TABLAS ------------------ #
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", background="#1e1e1e", foreground="white", fieldbackground="#1e1e1e", font=("Helvetica", 11))
style.map("Treeview", background=[("selected", "#4a4a4a")])

# ------------------ TABLAS DE TOKENS, ERRORES SINTÁCTICOS Y SEMÁNTICOS ------------------ #
tabla_tokens = crear_tabla("📘 Lexical Tokens:", ["Type", "Value", "Line", "Position"])
tabla_sintactico = crear_tabla("📙 Syntactic Errors:", ["Error", "Token", "Type", "Line"])

tabla_semantico_columnas = ["Error", "Description"]
tabla_semantico = crear_tabla("📕 Semantic Errors:", tabla_semantico_columnas)
tabla_semantico.column(0, width=150)
tabla_semantico.column(1, width=450)


# ------------------ EJECUCIÓN PRINCIPAL ------------------ #
ventana.mainloop()