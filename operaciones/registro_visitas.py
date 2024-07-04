import pandas as pd
from calculos import Calculos

class RegistroVisitas:
    def __init__(self):
        # Intenta cargar datos existentes; si no existe, crea DataFrames vacíos.
        self.df_pacientes=pd.read_excel('identidad_pacientes.xlsx', index_col=0,  dtype={'ID': str})
        try:
            self.df_historia_clinica = pd.read_excel('historia_clinica.xlsx', index_col=0,dtype={'ID': str})
            self.df_antropometria = pd.read_excel('antropometria.xlsx', index_col=0,dtype={'ID': str})
        except FileNotFoundError:
            self.df_historia_clinica = pd.DataFrame(columns=['ID', 'Número de Visita', 'Fecha de la Consulta', 'Notas', 'Diagnóstico', 'Tratamiento'])
            columns = ['ID', 'Número de Visita', 'Fecha de la Consulta', 'Amateur/Profesional',
                       'Peso kg', 'Estatura cm', '% de Grasa', '% de Agua', 'Kcal',
                       'Kg de Masa Muscular', 'Kg Masa Ósea', 'BMI', 'Triceps', 'Subescapular',
                       'Bíceps', 'Pectoral', 'Axilar', 'Cresta Iliaca', 'Supraespinal',
                       'Abdominal', 'Muslo Frontal', 'Pantorrilla Medial', 'Brazo Relajado',
                       'Brazo Contraído', 'Antebrazo', 'Pecho', 'Cintura', 'Abdomen',
                       'Cadera', 'Muslo1', 'Muslo Medio', 'Pantorrilla', 'Humero', 'Fémur',
                       'Estiloideo', 'Bimaleolar']
            self.df_antropometria = pd.DataFrame(columns=columns)
    
    def menu_registro_visitas(self):
        while True:
            print("\nMenú de Registro de Visitas")
            print("1. Añadir nueva visita")
            print("2. Editar registro de visita")
            print("3. Visualizar historial de visitas")
            print("4. Regresar al menú principal")

            opcion = input("Seleccione una opción: ")

            if opcion == '1':
               
                self.añadir_visita()
            elif opcion == '2':
                self.editar_registro()
            elif opcion == '3':
                self.visualizar_historial()
            elif opcion == '4':
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")
    
    
    
    def añadir_visita(self, id_paciente=None):
    # Si id_paciente no se proporciona directamente, solicitar al usuario que lo ingrese.
        if not id_paciente:
            id_paciente = input("Ingrese el ID del paciente para la visita: ")
            id_paciente = id_paciente.zfill(6)
            print(id_paciente)
            print(type(id_paciente))
          
    # Verificar si el ID proporcionado corresponde a un paciente registrado.
        if not self.df_pacientes['ID'].eq(id_paciente).any():
            print("Error: No existe un paciente con el ID proporcionado. Intente nuevamente.")
            return  # Terminar la ejecución si el ID no es válido.

    # Determinar automáticamente el número de visita para el paciente dado.
        if self.df_antropometria['ID'].eq(id_paciente).any():
            numero_visita = self.df_antropometria[self.df_antropometria['ID'] == id_paciente]['Número de Visita'].max() + 1
        else:
            numero_visita = 1  # Es la primera visita para este paciente.

        fecha_consulta = input("Ingrese la fecha de la consulta (YYYY-MM-DD): ")
        amateur_profesional = input("Ingrese si es Amateur o Profesional: ")

    # Recopilación de datos para la ficha clínica
        notas = input("Ingrese notas de la visita: ") or None
        diagnostico = input("Ingrese diagnóstico: ") or None
        tratamiento = input("Ingrese tratamiento: ") or None
        #id_paciente = str(id_paciente).zfill(6)
        datos_historia = {
            'ID': id_paciente,
            'Número de Visita': numero_visita,
            'Fecha de la Consulta': fecha_consulta,
            'Notas': notas,
            'Diagnóstico': diagnostico,
            'Tratamiento': tratamiento
        }
        self.df_historia_clinica = pd.concat([self.df_historia_clinica, pd.DataFrame([datos_historia])], ignore_index=True)
        self.df_historia_clinica.sort_values(by=['ID', 'Número de Visita'], inplace=True)

    # Recopilación de datos para antropometría
        peso = input("Ingrese el peso en kg: ") or None
        estatura = input("Ingrese la estatura en cm: ") or None
        grasa = input("Ingrese el porcentaje de grasa: ") or None
        agua = input("Ingrese el porcentaje de agua: ") or None
        kcal = input("Ingrese las Kcal: ") or None
        masa_muscular = input("Ingrese kg de masa muscular: ") or None
        masa_osea = input("Ingrese kg de masa ósea: ") or None
        bmi = input("Ingrese el BMI: ") or None
        triceps = input("Ingrese medida de triceps: ") or None
        subescapular = input("Ingrese medida subescapular: ") or None
        biceps = input("Ingrese medida de bíceps: ") or None
        pectoral = input("Ingrese medida pectoral: ") or None
        axilar = input("Ingrese medida axilar: ") or None
        cresta_iliaca = input("Ingrese medida cresta iliaca: ") or None
        supraespinal = input("Ingrese medida supraespinal: ") or None
        abdominal = input("Ingrese medida abdominal: ") or None
        muslo_frontal = input("Ingrese medida muslo frontal: ") or None
        pantorrilla_medial = input("Ingrese medida pantorrilla medial: ") or None
        brazo_relajado = input("Ingrese medida brazo relajado: ") or None
        brazo_contraido = input("Ingrese medida brazo contraído: ") or None
        antebrazo = input("Ingrese medida antebrazo: ") or None
        pecho = input("Ingrese medida pecho: ") or None
        cintura = input("Ingrese medida cintura: ") or None
        abdomen = input("Ingrese medida abdomen: ") or None
        cadera = input("Ingrese medida cadera: ") or None
        muslo1 = input("Ingrese medida muslo1: ") or None
        muslo_medio = input("Ingrese medida muslo medio: ") or None
        pantorrilla = input("Ingrese medida pantorrilla: ") or None
        humero = input("Ingrese medida humero: ") or None
        femur = input("Ingrese medida fémur: ") or None
        estiloideo = input("Ingrese medida estiloideo: ") or None
        bimaleolar = input("Ingrese medida bimaleolar: ") or None

        datos_antropometria = {
            'ID': id_paciente, 'Número de Visita': numero_visita, 'Fecha de la Consulta': fecha_consulta,
            'Amateur/Profesional': amateur_profesional, 'Peso kg': peso, 'Estatura cm': estatura, 
            '% de Grasa': grasa, '% de Agua': agua, 'Kcal': kcal, 'Kg de Masa Muscular': masa_muscular,
            'Kg Masa Ósea': masa_osea, 'BMI': bmi, 'Triceps': triceps, 'Subescapular': subescapular,
            'Bíceps': biceps, 'Pectoral': pectoral, 'Axilar': axilar, 'Cresta Iliaca': cresta_iliaca,
            'Supraespinal': supraespinal, 'Abdominal': abdominal, 'Muslo Frontal': muslo_frontal,
            'Pantorrilla Medial': pantorrilla_medial, 'Brazo Relajado': brazo_relajado,
            'Brazo Contraído': brazo_contraido, 'Antebrazo': antebrazo, 'Pecho': pecho,
            'Cintura': cintura, 'Abdomen': abdomen, 'Cadera': cadera, 'Muslo1': muslo1,
            'Muslo Medio': muslo_medio, 'Pantorrilla': pantorrilla, 'Humero': humero, 'Fémur': femur,
            'Estiloideo': estiloideo, 'Bimaleolar': bimaleolar
        }
    
        self.df_antropometria = pd.concat([self.df_antropometria, pd.DataFrame([datos_antropometria])], ignore_index=True)
        self.df_antropometria.sort_values(by=['ID', 'Número de Visita'], inplace=True)

        self.guardar_datos()
        print("Visita añadida exitosamente.")
        #Conecta con el módulo de calculos para correrlos automaticamente
        calculo = Calculos()
        calculo.funcion_ejecutora(id_paciente=id_paciente, numero_visita=numero_visita)

    def editar_registro(self):
        try:
            id_paciente = input("Ingrese el ID del paciente para editar su visita: ")
            numero_visita = input("Ingrese el número de visita que desea editar: ")

        # Convertir a formato adecuado
            id_paciente = id_paciente.zfill(6)
            numero_visita = int(numero_visita)  # Asegurarse que número de visita sea entero

        # Verificar si existe el registro
            if self.df_antropometria[(self.df_antropometria['ID'] == id_paciente) & (self.df_antropometria['Número de Visita'] == numero_visita)].empty:
                print("No se encontró la visita especificada.")
                return

        # Elegir el DataFrame a editar
            print("Seleccione el DataFrame a editar: 1 para Historia Clínica, 2 para Antropometría")
            eleccion = input("Ingrese su elección: ")
            if eleccion == '1':
                df_seleccionado = self.df_historia_clinica
            elif eleccion == '2':
                df_seleccionado = self.df_antropometria
            else:
                print("Opción no válida.")
                return

        # Mostrar datos actuales
            registro_actual = df_seleccionado[(df_seleccionado['ID'] == id_paciente) & (df_seleccionado['Número de Visita'] == numero_visita)]
            print("Registro actual:")
            print(registro_actual)

        # Elegir campo a editar
            campo = input("Ingrese el campo que desea editar: ")
            if campo not in df_seleccionado.columns:
                print("El campo no es válido.")
                return

            nuevo_valor = input(f"Ingrese el nuevo valor para {campo}: ")

        # Convertir el valor si es necesario, dependiendo del tipo de dato original
            tipo_original = df_seleccionado[campo].dtype
            if tipo_original == 'int64':
                nuevo_valor = int(nuevo_valor)
            elif tipo_original == 'float':
                nuevo_valor = float(nuevo_valor)

        # Editar el registro
            df_seleccionado.loc[(df_seleccionado['ID'] == id_paciente) & (df_seleccionado['Número de Visita'] == numero_visita), campo] = nuevo_valor
            self.guardar_datos()

            print("Registro actualizado con éxito.")
        except Exception as e:
            print(f"Error al editar el registro: {e}")

    def visualizar_historial(self): 
        try:
            id_paciente = input("Ingrese el ID del paciente para ver su historial de visitas: ")
            id_paciente = id_paciente.zfill(6)

        # Verificar si el paciente tiene registros
            if not self.df_antropometria[self.df_antropometria['ID'] == id_paciente].empty:
            # Seleccionar las columnas relevantes para mostrar en el resumen
                columnas = ['Número de Visita', 'Fecha de la Consulta', 'Peso kg', 'BMI', 'Bíceps', 'Muslo Medio']
                historial = self.df_antropometria[self.df_antropometria['ID'] == id_paciente][columnas]
                print("\nHistorial de visitas del paciente ID:", id_paciente)
                print(historial)
            else:
                print("No se encontraron visitas para el ID proporcionado.")
        except Exception as e:
            print(f"Error al visualizar el historial: {e}")


    def guardar_datos(self):
    # Guardar DataFrames en archivos de Excel
        self.df_antropometria.to_excel('antropometria.xlsx')
        self.df_historia_clinica.to_excel('historia_clinica.xlsx')
