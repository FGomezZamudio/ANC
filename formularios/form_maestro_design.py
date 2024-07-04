import tkinter as tk
from tkinter import font # sirve para manejar los tipos de fuentes de letras
from config import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA
import util.util_ventana as util_ventana
import util.util_imagenes as util_img
from formularios.form_gestion_pacientes import FormularioGestionPacientes
from formularios.form_registro_visitas import FormularioRegistroVisitas
from formularios.form_reportes import FormularioReportes

class FormularioMaestroDesign (tk.Tk): 
     
    def __init__(self):
        super().__init__()
        self.logo = util_img.leer_imagen("./imagenes/anc_logo.png", (553,561))
        self.perfil = util_img.leer_imagen("./imagenes/foto_perfil.png", (70, 91))
        self.config_window()
        self.paneles()
        self.controles_barra_superior()
        self.controles_menu_lateral()
        self.controles_cuerpo_principal()
    
    def config_window(self):
        self.title("CENTRO DE GESTIÓN NUTRICIONAL Y DEPORTIVA")
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

        self.labeltitulo = tk.Label (self.barra_superior, text = "Método ANC")
        self.labeltitulo.config(fg = "#fff", font = ("Roboto", 15), bg= COLOR_BARRA_SUPERIOR, pady =10, width =16)
        self.labeltitulo.pack (side =tk.LEFT)

        self.buttonMenuLateral = tk.Button(self.barra_superior,text="\uf0c9",command = self.toggle_panel, font = font_awesome,bd=0,bg=COLOR_BARRA_SUPERIOR,fg="white")
        self.buttonMenuLateral.pack(side=tk.LEFT)

        self.labeltitulo=tk.Label(self.barra_superior, text="felipe.gomez@anc.com.mx")
        self.labeltitulo.config(fg="#fff", font=("Roboto",12), bg=COLOR_BARRA_SUPERIOR, padx=10, width=20)
        self.labeltitulo.pack(side=tk.RIGHT)

    def controles_menu_lateral(self):
        ancho_menu= 20
        alto_menu = 2
        font_awesome = font.Font(family = "FontAwesome", size =12)
        self.labelperfil = tk.Label(self.menu_lateral, image = self.perfil, bg = COLOR_MENU_LATERAL)
        self.labelperfil.pack(side =tk.TOP, pady = 30)
        # A continuación se van a instanciar todos los botones del menú lateral

        self.boton_gestion_pacientes = tk.Button(self.menu_lateral, command=self.abrir_gestion_pacientes)
        self.boton_registro_visitas = tk.Button(self.menu_lateral, command = self.abrir_registro_visitas)
        self.boton_reportes = tk.Button(self.menu_lateral, command = self.abrir_reportes)
        self.boton_salir_aplicacion = tk.Button(self.menu_lateral)
        self.boton_salir_aplicacion.config(text ="\uf060   Salir", font = font_awesome,
                     bd=0, bg=COLOR_MENU_LATERAL, fg = "white", width =ancho_menu, height = alto_menu)
        self.boton_salir_aplicacion.pack(side=tk.BOTTOM)
        self.bind_hover_events(self.boton_salir_aplicacion)

        #Configuración y empaquetamiento de los botones

        buttons_info = [
            ("Gestión Pacientes", "\uf007", self.boton_gestion_pacientes),
            ("Registro Visitas", "\uf274", self.boton_registro_visitas),
            ("Reportes","\uf46d", self.boton_reportes),
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
        self.labellogo = tk.Label(self.cuerpo_principal, image = self.logo, bg = COLOR_CUERPO_PRINCIPAL)
        self.labellogo.pack(side =tk.TOP, pady = 30)

    def abrir_gestion_pacientes(self):
        FormularioGestionPacientes()
    def abrir_registro_visitas(self):
        FormularioRegistroVisitas()
    def abrir_reportes(self):
        FormularioReportes()