import tkinter as tk
from tkinter import font
import util.util_ventana as util_ventana
from config import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA, COLOR_CUERPO


class FormularioGestionPacientes(tk.Toplevel): 
    def __init__(self) -> None:
        super().__init__()
        self.config_window()
        self.paneles()
        self.controles_barra_superior()
        self.controles_menu_lateral()


    def config_window(self):
        self.title("MÉTODO ANC")
        self.iconbitmap("./imagenes/anc_logo.ico")
        w, h = 1024, 600
        self.geometry("%dx%d+0+0" % (w, h))
        util_ventana.centrar_ventana(self, w, h)

    def paneles(self):
        self.barra_superior = tk.Frame (self, bg = COLOR_BARRA_SUPERIOR, height= 50) # Un Frame es un widget que sirve como contenedor para otros widgets, se puede entender como un subconjunto de wigdgets
        self.barra_superior.pack(side = tk.TOP, fill= "both") # sirve para ubicar el Frame barra_superior en la ventana 

        self.menu_lateral = tk.Frame(self, bg = COLOR_MENU_LATERAL, width = 150)
        self.menu_lateral.pack (side = tk.LEFT, fill= "both", expand = False)
        
        
        self.cuerpo_principal = tk.Frame (self, bg = COLOR_CUERPO_PRINCIPAL)
        self.cuerpo_principal.pack( side = tk.RIGHT, fill ="both", expand =True)

    def controles_barra_superior(self):
        font_awesome =font.Font( family = "FontAwesome", size = 12)

        self.labeltitulo = tk.Label (self.barra_superior, text = "Gestión de los pacientes")
        self.labeltitulo.config(fg = "#fff", font = ("Roboto", 12), bg= COLOR_BARRA_SUPERIOR, pady =10, width =20)
        self.labeltitulo.pack (side =tk.LEFT, padx = 10)

        self.buttonMenuLateral = tk.Button(self.barra_superior,text="\uf0c9",command = self.toggle_panel, font = font_awesome,bd=0,bg=COLOR_BARRA_SUPERIOR,fg="white")
        self.buttonMenuLateral.pack(side=tk.LEFT)

        self.labeltitulo=tk.Label(self.barra_superior, text="felipe.gomez@anc.com.mx")
        self.labeltitulo.config(fg="#fff", font=("Roboto",12), bg=COLOR_BARRA_SUPERIOR, padx=10, width=20)
        self.labeltitulo.pack(side=tk.RIGHT)

    def controles_menu_lateral(self):
        ancho_menu= 20
        alto_menu = 2
        font_awesome = font.Font(family = "FontAwesome", size =12)

        self.boton_añadir_paciente = tk.Button(self.menu_lateral, command = self.controles_cuerpo_principal) # command tiene que llamar a la función correspondiente del back que es añadir pacientes
        self.boton_editar_informacion = tk.Button(self.menu_lateral)
        self.boton_mostrar_pacientes = tk.Button(self.menu_lateral)
        self.boton_mostrar_id = tk.Button(self.menu_lateral)
        self.boton_regresar =tk.Button(self.menu_lateral)
        self.boton_regresar.config(text ="\uf060   Salir", font = font_awesome,
                     bd=0, bg=COLOR_MENU_LATERAL, fg = "white", width =ancho_menu, height = alto_menu)
        self.boton_regresar.pack(side=tk.BOTTOM)
        self.bind_hover_events(self.boton_regresar)

        buttons_info = [
            ("Añadir paciente", "\uf2b9", self.boton_añadir_paciente),
            ("Editar información", "\uf044", self.boton_editar_informacion),
            ("Mostrar pacientes","\uf03a", self.boton_mostrar_pacientes),
            ("Mostrar ID","\uf2c2", self.boton_mostrar_id)
            ]
        
        for text, icon, button in buttons_info:
            self.configurar_boton_menu(button, text, icon, font_awesome, ancho_menu, alto_menu)

    def configurar_boton_menu(self,button, text, icon, font_awesome, ancho_menu, alto_menu):
        button.config(text = f"  {icon}  {text}", anchor="w", font = font_awesome,
                     bd=0, bg=COLOR_MENU_LATERAL, fg = "white", width =ancho_menu, height = alto_menu)
        button.pack(side=tk.TOP)
        self.bind_hover_events(button)

    def bind_hover_events(self,button):
        button.bind("<Enter>", lambda event: self.on_enter(event, button))
        button.bind("<Leave>", lambda event: self.on_leave(event, button))
   
    def on_enter(self,event,button):
        button.config(bg=COLOR_MENU_CURSOR_ENCIMA, fg="white")
   
    def on_leave (self,event,button):
        button.config(bg=COLOR_MENU_LATERAL, fg="white")
    
    
    
    def toggle_panel(self):
        if self.menu_lateral.winfo_ismapped():
            self.menu_lateral.pack_forget()
        else:
            self.menu_lateral.pack(side=tk.LEFT, fill="y")
          
    def controles_cuerpo_principal(self):
        self.paneles_cuerpo_principal()
        self.widgets_cuerpo_principal()

    def paneles_cuerpo_principal(self):
        self.work_top = tk.Frame(self.cuerpo_principal, bg=COLOR_CUERPO_PRINCIPAL, height=50)
        self.work_top.pack(side=tk.TOP, fill="both")

        self.work_bottom = tk.Frame(self.cuerpo_principal, bg=COLOR_BARRA_SUPERIOR, height=30)
        self.work_bottom.pack(side=tk.BOTTOM, fill="both", expand=False)
    
        self.panel1 = tk.Frame(self.cuerpo_principal, bg=COLOR_CUERPO, width=218)
        self.panel1.pack(side=tk.LEFT, fill="both", expand=True)
    
        self.panel2 = tk.Frame(self.cuerpo_principal, bg=COLOR_CUERPO, width=218)
        self.panel2.pack(side=tk.LEFT, fill="both", expand=True)  # Cambiado a tk.LEFT para que se alinee con work_left
    
        self.panel3 = tk.Frame(self.cuerpo_principal, bg=COLOR_CUERPO, width=218)
        self.panel3.pack(side=tk.LEFT, fill="both", expand=True)

        self.panel4 = tk.Frame(self.cuerpo_principal, bg=COLOR_CUERPO, width=218)
        self.panel4.pack(side=tk.LEFT, fill="both", expand=True)
      

    def widgets_cuerpo_principal(self):
        font_awesome = font.Font(family = "FontAwesome", size =12)
        self.labeltitulo_cuerpo = tk.Label(self.work_top, text="Datos generales del paciente")
        self.labeltitulo_cuerpo.config(fg="#030303", font=("Impact", 12), bg=COLOR_CUERPO_PRINCIPAL, pady=10, width=40)
        self.labeltitulo_cuerpo.pack(side=tk.LEFT, padx= 250)

        self.boton_guardar_registro =tk.Button(self.work_bottom)
        self.boton_guardar_registro.config(text ="Guardar Registro \uf0c7", font = font_awesome,
                     bd=0, bg="#33f52c", fg = "white", width =20, height = 2)
        self.boton_guardar_registro.pack(side=tk.BOTTOM, anchor = "center", pady = 10)

        widgets_info = [
            (self.panel1, "Nombre"),
            (self.panel1, "Sexo"),
            (self.panel1, "Fecha de nacimiento"),
            (self.panel1, "Estado civil"),
            (self.panel3, "Ocupación"),
            (self.panel3, "Correo electrónico"),
            (self.panel3, "Celular"),
            (self.panel3, "Red social"),
        ]
    
        for panel, etiqueta in widgets_info:
            etiq = tk.Label(panel, text=etiqueta)
            etiq.config(fg="#030303", font=("Roboto", 12), bg=COLOR_CUERPO, width=20)
            etiq.pack(side=tk.TOP, pady=30, anchor="w")
        

        entradas = [ ("nombre", self.panel2),
                    ("sexo", self.panel2),
                    ("fecha_de_nacimiento", self.panel2),
                    ("estado_civil", self.panel2),
                    ("ocupacion", self.panel4),
                    ("correo", self.panel4),
                    ("celular", self.panel4),
                    ("red_social", self.panel4),
                    ]
        for caja, panel  in entradas:
            caja = tk.Entry(panel, bg= COLOR_CUERPO_PRINCIPAL, width= 20 )
            caja.pack(side=tk.TOP, anchor = "w", pady =33)