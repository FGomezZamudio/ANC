import pandas as pd
import unidecode
from registro_visitas import RegistroVisitas

class GestionPacientes:
    def __init__(self):
        # Intenta cargar datos existentes desde 'identidad_pacientes.xlsx'; si no existe, crea un DataFrame vacío.
        try:
            self.df_pacientes = pd.read_excel('identidad_pacientes.xlsx', index_col=0, dtype={'ID': str})
            max_id = self.df_pacientes['ID'].max()
            self.id_counter = int(max_id)+1  # Establece el contador de ID al máximo existente + 1
            
        except FileNotFoundError:
            self.df_pacientes = pd.DataFrame(columns=['ID', 'Nombre', 'Sexo', 'Fecha de Nacimiento', 'Edad', 'Estado Civil', 'Ocupación', 'Correo Electrónico', 'Número de Celular', 'Cuenta de Red Social'])
            self.id_counter = 1  # Inicia el contador de ID

    

    def añadir_paciente(self):
        try:
            nombre = input("Ingrese el nombre del paciente: ")
            sexo = input("Ingrese el sexo del paciente: ")
            fecha_nacimiento = input("Ingrese la fecha de nacimiento del paciente (YYYY-MM-DD): ")
            edad = input("Ingrese la edad del paciente: ")
            estado_civil = input("Ingrese el estado civil del paciente: ")
            ocupacion = input("Ingrese la ocupación del paciente: ")
            correo = input("Ingrese el correo electrónico del paciente: ")
            celular = input("Ingrese el número de celular del paciente: ")
            red_social = input("Ingrese la cuenta de red social del paciente: ")

            nuevo_id = str(self.id_counter).zfill(6)  # Asignar ID antes de incrementar el contador
            self.id_counter += 1  # Incrementar primero antes de usarlo

            datos_paciente = {
                'ID': nuevo_id, 'Nombre': nombre, 'Sexo': sexo, 
                'Fecha de Nacimiento': fecha_nacimiento, 'Edad': edad, 'Estado Civil': estado_civil, 
                'Ocupación': ocupacion, 'Correo Electrónico': correo, 'Número de Celular': celular, 
                'Cuenta de Red Social': red_social
            }
            datos_paciente1 = pd.DataFrame([datos_paciente])
            self.df_pacientes = pd.concat([self.df_pacientes, datos_paciente1], ignore_index=True)
            self.guardar_datos()  # Guarda los cambios en el archivo.
            
            print("Paciente añadido exitosamente. Redirigiendo a añadir visita...")
           
            registro_visitas = RegistroVisitas()
            registro_visitas.añadir_visita(id_paciente=nuevo_id)  # Usar el nuevo_id directamente
            #registro_visitas.añadir_visita(id_paciente=int(nuevo_id))
            return nuevo_id
        except Exception as e:
            print(f"Ocurrió un error al añadir el paciente: {e}")
            return None


      
      
       
            
    
    def editar_paciente(self):
        id_paciente1 = input("Ingrese el ID del paciente que desea editar: ")
        id_paciente = id_paciente1.zfill(6)
        if id_paciente in self.df_pacientes['ID'].values:
            print("Información actual del paciente:")
            print(self.df_pacientes[self.df_pacientes['ID'] == id_paciente])
        
            campo = input("Ingrese el campo que desea editar (Nombre, Sexo, Fecha de Nacimiento, etc.): ")
            nuevo_valor = input(f"Ingrese el nuevo valor para {campo}: ")
        
        # Verificar que el campo existe en el DataFrame
            if campo in self.df_pacientes.columns:
                self.df_pacientes.loc[self.df_pacientes['ID'] == id_paciente, campo] = nuevo_valor
                self.guardar_datos()
                print("Información actualizada con éxito.")
            else:
                print("Campo no válido.")
        else:
            print("No se encontró un paciente con ese ID.")

    
    def buscar_por_nombre(self):
        nombre_input = input("Ingrese el nombre del paciente a buscar: ")
        nombre_normalizado = unidecode.unidecode(nombre_input).lower()  # Normalizar y convertir a minúsculas

    # Aplicar normalización y conversión a minúsculas a la columna de nombres
        nombres_normalizados = self.df_pacientes['Nombre'].apply(lambda x: unidecode.unidecode(x).lower() if isinstance(x, str) else "")

    # Buscar coincidencias en nombres normalizados
        resultados = self.df_pacientes[nombres_normalizados.str.contains(nombre_normalizado, case=False, na=False)]

        if not resultados.empty:
            print("Resultados encontrados:")
            print(resultados[['ID', 'Nombre']])
        else:
            print("No se encontraron pacientes con ese nombre.")
    
    def guardar_datos(self):
        # Guarda el DataFrame actualizado en 'identidad_pacientes.xlsx'.
        self.df_pacientes.to_excel('identidad_pacientes.xlsx')

    def mostrar_pacientes(self):
        # Muestra todos los registros de pacientes en la consola.
        print(self.df_pacientes)


