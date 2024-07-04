import pandas as pd
from formulas_grasa import FormulasGrasa

class Calculos:
    def __init__(self):
        # Intentar cargar los DataFrames desde archivos Excel.
        self.cargar_datos()

    def cargar_datos(self):
        try:
            self.df_antropometria = pd.read_excel('antropometria.xlsx', index_col=0, dtype={'ID': str})
            print("Datos de antropometría cargados correctamente.")
        except FileNotFoundError:
            self.df_antropometria = None
            print("Archivo de antropometría no encontrado. Asegúrese de que el archivo exista.")
        try:
            self.df_historia_clinica = pd.read_excel('historia_clinica.xlsx', index_col=0, dtype={'ID': str})
            print("Datos de historia clinica cargados correctamente.")
        except FileNotFoundError:
            self.df_historia_clinica = None
            print("Archivo historia_clinica no encontrado. Asegúrese de que el archivo exista.")
        try:
            self.df_identidad_pacientes = pd.read_excel('identidad_pacientes.xlsx', index_col=0, dtype={'ID': str})
            print("Datos de historia clínica cargados correctamente.")
        except FileNotFoundError:
            self.df_identidad_pacientes = None
            print("Archivo de historia clínica no encontrado. Asegúrese de que el archivo exista.")
        try:
            self.df_composicion = pd.read_excel('composicion.xlsx', index_col=0, dtype={'ID': str})    
        except FileNotFoundError:
            self.df_composicion = pd.DataFrame(columns=["ID","Numero de visita","Kg de grasa","Porcentaje de grasa","Kg de músculo","Porcentaje de músculo","Kg de hueso","Porcentaje de hueso","Kg de tejido residual","Porcentaje de tejido residual","Endomorfo","Mesomorfo","Ectomorfo","Clasificación de somatotipo","X","Y","zPeso","zBrazo Contraído","zKg de grasa","zCintura","zCadera","zKg de musculo","IMC","Clasificacion de IMC","Indice cintura/cadera","Clasificación cintura/cadera","TER"])

#Las salidas de las siguientes funciones conviene que sea un diccionario así cuando se 
#llame a la función reporte_composicion_corporal y se construya el dataframe que será la base para el front
#cada clave de estos diccionarios será una columna

    def funcion_ejecutora(self, id_paciente, numero_visita):
        self.datos_generales(id_paciente, numero_visita)
        composicion_corporal = self.calculo_composicion_corporal(id_paciente, numero_visita)
        somatotipo = self.calculo_somatotipo(id_paciente, numero_visita)
        zscore = self.calculo_zscore(id_paciente, numero_visita,composicion_corporal)
        riesgo_cardiovascular = self.calculo_riesgo_cardiovascular(id_paciente, numero_visita)
        self.guardar_resultados_calculos( id_paciente, numero_visita, composicion_corporal, somatotipo, zscore, riesgo_cardiovascular)

    def datos_generales(self, id_paciente, numero_visita):
        fecha_proxima_consulta=input("Ingrese la fecha de la siguiente consulta (YYYY-MM-DD): ")
    # Obtener los datos del paciente desde el DataFrame de identidad_pacientes
        datos_paciente = self.df_identidad_pacientes[self.df_identidad_pacientes['ID'] == id_paciente]

    # Extraer la fecha de la primera visita
        primera_visita = self.df_antropometria[self.df_antropometria['Número de Visita'] == 1]
        fecha_primera_visita = primera_visita['Fecha de la Consulta'].iloc[0] if not primera_visita.empty else "Desconocido"


    # Obtener datos desde el DataFrame de antropometría para la visita actual
        datos_antropometria = self.df_antropometria[(self.df_antropometria['ID'] == id_paciente) & 
                                                (self.df_antropometria['Número de Visita'] == numero_visita)]

    # Extraer datos como estatura y peso de antropometría
        peso_actual = datos_antropometria['Peso kg'].iloc[0] if not datos_antropometria.empty else "Desconocido"
        estatura_actual = datos_antropometria['Estatura cm'].iloc[0] if not datos_antropometria.empty else "Desconocido"

    # Compilar todos los datos generales
        datos_generales = {
            "Nombre": datos_paciente['Nombre'].iloc[0],
            "Sexo": datos_paciente['Sexo'].iloc[0],
            "Peso": peso_actual,
            "Estatura": estatura_actual,
            "Edad": datos_paciente['Edad'].iloc[0],
            "Fecha de nacimiento": datos_paciente['Fecha de Nacimiento'].iloc[0],
            "Fecha de la primera consulta": fecha_primera_visita,
            "Fecha de la próxima consulta": fecha_proxima_consulta
        }

        return datos_generales
    
    def calculo_composicion_corporal(self, id_paciente, numero_visita):
        # Extraer datos necesarios del DataFrame de antropometría.
        datos = self.df_antropometria[(self.df_antropometria['ID'] == id_paciente) & 
                                      (self.df_antropometria['Número de Visita'] == numero_visita)]
        paciente = self.df_identidad_pacientes[(self.df_identidad_pacientes["ID"] == id_paciente)]
        sexo = paciente["Sexo"].iloc[0].capitalize()
        edad = paciente["Edad"].iloc[0]
        if datos.empty:
            print("Datos no encontrados")
            return pd.DataFrame()

        # Definición de variables necesarias para los cálculos.
        triceps = datos['Triceps'].iloc[0]
        subescapular = datos['Subescapular'].iloc[0]
        biceps = datos['Bíceps'].iloc[0]
        cresta_iliaca = datos['Cresta Iliaca'].iloc[0]
        pectoral = datos['Pectoral'].iloc[0]
        axilar = datos['Axilar'].iloc[0]
        abdominal = datos['Abdominal'].iloc[0]
        muslo_frontal = datos['Muslo Frontal'].iloc[0]
        pantorrilla_medial = datos['Pantorrilla Medial'].iloc[0]
        supraespinal = datos['Supraespinal'].iloc[0]
        estatura = datos['Estatura cm'].iloc[0]
        peso = datos['Peso kg'].iloc[0]
        estiloideo = datos['Estiloideo'].iloc[0]
        bimaleolar = datos['Bimaleolar'].iloc[0]
        categoria = datos["Amateur/Profesional"].iloc[0]
        brazo_relajado = datos["Brazo Relajado"].iloc[0]
        
        # Llamada a la función que selecciona el conjunto de fórmulas adecuado.
        porcentaje_grasa = self.calculo_grasa(categoria, sexo,triceps, subescapular, biceps, cresta_iliaca, pectoral,axilar, abdominal, muslo_frontal, pantorrilla_medial,supraespinal, estatura, brazo_relajado, edad)
        kg_grasa = peso*(porcentaje_grasa/100)
        kg_hueso = self.calculo_hueso(estatura, estiloideo, bimaleolar)
        porcentaje_hueso = (kg_hueso/peso)*100
        porcentaje_residual = 24 if sexo == "Hombre" else 21
        kg_residual = peso * (porcentaje_residual/100)
        porcentaje_musculo = 100 - porcentaje_grasa - porcentaje_hueso - porcentaje_residual
        kg_musculo = peso * (porcentaje_musculo/100)
       
        composicion_corporal = {
            'Kg de grasa': kg_grasa,
            'Porcentaje de grasa': porcentaje_grasa,
            'Kg de músculo': kg_musculo,
            'Porcentaje de músculo': porcentaje_musculo,
            'Kg de hueso': kg_hueso,
            'Porcentaje de hueso': porcentaje_hueso,
            'Kg de tejido residual': kg_residual,
            'Porcentaje de tejido residual': porcentaje_residual

            
        }

        return composicion_corporal     

    def calculo_grasa(self, categoria, sexo, triceps, subescapular, biceps, cresta_iliaca, pectoral,axilar, abdominal, muslo_frontal, pantorrilla_medial, supraespinal,estatura, brazo_relajado, edad):
        # Elección del conjunto de fórmulas basado en la categoría y sexo.
        if categoria == 'Profesional' and sexo == 'Hombre':
            return FormulasGrasa.calcular_grasa_profesional_hombre(triceps, subescapular, axilar, abdominal, pantorrilla_medial, supraespinal)
        elif categoria == 'Profesional' and sexo == 'Mujer':
            return  FormulasGrasa.calcular_grasa_profesional_mujer(triceps, subescapular, biceps, abdominal, muslo_frontal, pantorrilla_medial, supraespinal, estatura, brazo_relajado)
        elif categoria == 'Amateur' and sexo == 'Hombre':
            return  FormulasGrasa.calcular_grasa_amateur_hombre(triceps, subescapular, biceps, cresta_iliaca, pectoral, axilar, abdominal, muslo_frontal, pantorrilla_medial, edad)
        elif categoria == 'Amateur' and sexo == 'Mujer':
             return  FormulasGrasa.calcular_grasa_amateur_mujer(triceps, subescapular, biceps, cresta_iliaca, pectoral, axilar, abdominal, muslo_frontal, pantorrilla_medial, supraespinal, estatura, brazo_relajado, edad)
        else:
            print("Combinación de categoría y sexo no válida.")
            return None
    def calculo_hueso(self,estatura, estiloideo, bimaleolar):
        kg_hueso = 3.02*((estatura/100)**2*(estiloideo/100)*(bimaleolar/100)*400)**0.712 
        return kg_hueso
    

    def calculo_somatotipo(self, id_paciente, numero_visita):
        datos = self.df_antropometria[(self.df_antropometria['ID'] == id_paciente) & 
                                      (self.df_antropometria['Número de Visita'] == numero_visita)]
        triceps = datos['Triceps'].iloc[0]
        subescapular = datos['Subescapular'].iloc[0]
        supraespinal = datos["Supraespinal"].iloc[0]
        estatura = datos['Estatura cm'].iloc[0]
        humero = datos["Humero"].iloc[0]
        femur = datos["Fémur"].iloc[0]
        brazo_contraido = datos["Brazo Contraído"].iloc[0]
        peso = datos["Peso kg"].iloc[0]
        #calculo endomorfo
        endocorr = (triceps + subescapular + supraespinal)*(170.18/estatura)
        endomorfo = 0.7182 + 0.1451*endocorr - 0.00068*endocorr**2 + 0.0000014*endocorr**3
        #calculo mesomorfo
        brazo_corr = brazo_contraido - (triceps/10)
        mesomorfo = 0.858*humero + 0.601*femur + 0.188*endocorr + 0.161*brazo_corr - 0.131*estatura + 4.5
        #calculo ectomorfo
        hwr = estatura/(peso**0.333)
        if hwr > 38.25:
            ectomorfo = 0.732*hwr - 28.58
        else:
            ectomorfo = 0.463*hwr - 17.63
        #calculo de coordenadas somatograma
        x = ectomorfo - endomorfo
        y = 2*mesomorfo - (endomorfo + ectomorfo)
    # Ejemplo de implementación temporal
        somatotipo= {
            "Endomorfo": endomorfo,
            "Mesomorfo": mesomorfo,
            "Ectomorfo": ectomorfo,
            "Clasificación de somatotipo": "Indeterminado",
            "X": x,  # Si 'X' y 'Y' son parte de las coordenadas del somatotipo
            "Y": y
        }
        return somatotipo

    def calculo_zscore(self, id_paciente, numero_visita, composicion_corporal):
    # Ejemplo de implementación temporal
        datos = self.df_antropometria[(self.df_antropometria['ID'] == id_paciente) & 
                                      (self.df_antropometria['Número de Visita'] == numero_visita)]
        peso = datos["Peso kg"].iloc[0]
        brazo_contraido = datos["Brazo Contraído"].iloc[0]
        kg_grasa = composicion_corporal["Kg de grasa"]
        cintura = datos["Cintura"].iloc[0]
        cadera = datos["Cadera"].iloc[0]
        kg_musculo = composicion_corporal["Kg de músculo"]
        estatura = datos['Estatura cm'].iloc[0]
        # calculo del zscore
        estatura_corr = (170.18/estatura)**3
        zpeso = (peso*estatura_corr - 64.58)/8.6
        zbrazo_contraido = (brazo_contraido*estatura_corr - 29.41)/2.37
        zkg_grasa = (kg_grasa*estatura_corr - 12.13)/3.25
        zcintura = (cintura*estatura_corr - 71.91)/4.45
        zcadera = (cadera*estatura_corr - 94.67)/5.58
        zkg_musculo = (kg_musculo*estatura_corr - 25.55)/2.99
        
        zscore = {
            "zPeso": zpeso,
            "zBrazo Contraído": zbrazo_contraido,
            "zKg de grasa": zkg_grasa,
            "zCintura": zcintura,
            "zCadera": zcadera,
            "zKg de musculo": zkg_musculo
        }
        return zscore

    def calculo_riesgo_cardiovascular(self, id_paciente, numero_visita):
    # Ejemplo de implementación temporal
        datos = self.df_antropometria[(self.df_antropometria['ID'] == id_paciente) & 
                                      (self.df_antropometria['Número de Visita'] == numero_visita)]
        peso = datos ["Peso kg"].iloc[0]
        estatura = datos["Estatura cm"].iloc[0]
        cintura = datos["Cintura"].iloc[0]
        cadera = datos["Cadera"].iloc[0]
        subescapular = datos['Subescapular'].iloc[0]
        cresta_iliaca = datos['Cresta Iliaca'].iloc[0]
        triceps = datos['Triceps'].iloc[0]
        biceps = datos['Bíceps'].iloc[0]
        pantorrilla_medial = datos['Pantorrilla Medial'].iloc[0]

        imc = peso/((estatura/100)**2)

        if imc <= 18.5:
            clasifimc = "Bajo"
        elif imc > 18.5 and imc < 24.9:
            clasifimc = "Normal"
        elif imc >= 24.9 and imc < 29.9:
            clasifimc = "Sobrepeso"
        elif imc >= 29.9:
            clasifimc = "Obesidad"
        
        icc = cintura/cadera

        if icc < 0.71:
            clasificc = "Bajo"
        elif icc >= 0.71 and icc < 0.93:
            clasificc = "Moderado"
        elif icc >= 0.93:
            clasificc = "Alto"

        ter = (subescapular + cresta_iliaca) - (triceps + biceps + pantorrilla_medial)

        riesgo_cardiovascular = {
            "IMC": imc,
            "Clasificacion de IMC": clasifimc,
            "Indice cintura/cadera": icc,
            "Clasificación cintura/cadera": clasificc,
            "TER": ter  
        }
        return riesgo_cardiovascular


    def guardar_resultados_calculos(self, id_paciente, numero_visita, composicion_corporal, somatotipo, zscore, riesgo_cardiovascular):
    # Crear un nuevo registro con todos los datos necesarios
       
        nuevo_registro = {
            "ID": id_paciente,
            "Numero de visita": numero_visita,
            **composicion_corporal,  # Desempaqueta el diccionario de composición corporal
            **somatotipo,  # Desempaqueta el diccionario de somatotipo
            **zscore,  # Desempaqueta el diccionario de z-scores
            **riesgo_cardiovascular  # Desempaqueta el diccionario de riesgo cardiovascular
        }

    # Convertir el diccionario a DataFrame para poder concatenar
        nuevo_registro_df = pd.DataFrame([nuevo_registro])

    # Concatenar el nuevo registro al DataFrame existente
        self.df_composicion = pd.concat([self.df_composicion, nuevo_registro_df], ignore_index=True)

    # Ordenar los datos por ID y Número de visita por si se requiere
        self.df_composicion.sort_values(by=['ID', 'Numero de visita'], inplace=True)

    # Opcional: guardar el DataFrame actualizado en un archivo, si es necesario
        self.df_composicion.to_excel('composicion.xlsx', index=False)

        




    def plan_nutricional(self):
        pass
        # Implementación de plan nutricional aquí
