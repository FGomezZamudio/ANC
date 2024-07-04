import statistics
import math
class FormulasGrasa:
    @staticmethod
    def calcular_grasa_profesional_hombre(triceps, subescapular, axilar, abdominal, pantorrilla_medial, supraespinal):
        # Método Forsyth
        DCf=1.10647-(0.00162*subescapular)- (0.00144*abdominal) - (0.00077*triceps) + (0.00071*axilar)
        Forsyth = (454/DCf)-414.2
        # Método WithersH

        suma_pliegues= triceps + subescapular + supraespinal + pantorrilla_medial
        DCw= 1.17484 - 0.07229*math.log10(suma_pliegues)
        WithersH = (495/DCw) - 450


        porcentaje_grasa = statistics.mean([Forsyth, WithersH])  # Sustituir con la fórmula real
        return porcentaje_grasa

    @staticmethod
    def calcular_grasa_profesional_mujer(triceps, subescapular, biceps, abdominal, muslo_frontal, pantorrilla_medial, supraespinal, estatura, brazo_relajado):
        # Método WhitersM
        suma_pliegues= triceps + subescapular + biceps + supraespinal + abdominal + muslo_frontal + pantorrilla_medial
        DCwm = 1.0988 - 0.0004 * suma_pliegues
        WithersM = (495/DCwm) - 450

        # Método Lewis

        DCl = 0.97845 - 0.0002*triceps + 0.00088*estatura - 0.00122* subescapular - 0.00234*brazo_relajado
        Lewis = (495/DCl) - 450

    
        porcentaje_grasa = statistics.mean([WithersM, Lewis])  # Sustituir con la fórmula real
        return porcentaje_grasa

    @staticmethod
    def calcular_grasa_amateur_hombre(triceps, subescapular, biceps, cresta_iliaca, pectoral, axilar, abdominal, muslo_frontal, pantorrilla_medial, edad):
        # Método DurninH
        suma_plieguesd = triceps + subescapular + biceps + cresta_iliaca
        DCd = 1.1765 - 0.0744 * math.log10(suma_plieguesd)
        DurninH = (495/DCd) - 450
        # Método JacksonH
        suma_plieguesj = pectoral + axilar + triceps + subescapular + abdominal + cresta_iliaca + muslo_frontal
        DCj= 1.112 - 0.00043499*suma_plieguesj + 0.00000055*(suma_plieguesj)**2 - 0.00028826*edad
        JacksonH = (495/DCj) - 450
        # método WilmarH
        DCw = 1.08543 - 0.000886* abdominal - 0.0004* muslo_frontal
        WilmarH =  (495/DCw) - 450
        # Método Sloan
        DCs = 1.1043 - 0.001327*muslo_frontal - 0.00131*subescapular
        SloanH = (457/DCs) - 414.2
        #Método Thorland
        suma_plieguest = triceps + subescapular + axilar + abdominal + muslo_frontal + pantorrilla_medial
        DCt = 1.1091 - 0.00052* suma_plieguest - 0.00000032* (suma_plieguest)**2
        ThorlandH = (495/DCt) - 450
        porcentaje_grasa = statistics.mean([DurninH, JacksonH, WilmarH, SloanH, ThorlandH])  # Sustituir con la fórmula real
        return porcentaje_grasa

    @staticmethod
    def calcular_grasa_amateur_mujer(triceps, subescapular, biceps, cresta_iliaca, pectoral, axilar, abdominal, muslo_frontal, pantorrilla_medial, supraespinal, estatura, brazo_relajado, edad):
        # Método DurninM
        suma_plieguesd = triceps + subescapular + biceps + cresta_iliaca
        DCdm = 1.1567 - 0.0717*math.log10(suma_plieguesd)
        DurninM = (495/DCdm) - 450
        # Método JacksonM
        suma_plieguesj= triceps + cresta_iliaca + abdominal + muslo_frontal
        DCjm= 1.096095 - 0.0006952* suma_plieguesj + 0.0000011* (suma_plieguesj)**2 - 0.0000714*edad
        JacksonM = (495/DCjm) - 450
        # Método WilamrM
        DCw = 1.06234 - 0.00068*subescapular - 0.00039*triceps - 0.00025*muslo_frontal
        WilmarM = (495/DCw) - 450
        #Método SloanM
        DCs = 1.0764 - 0.00081*cresta_iliaca - 0.00088*triceps
        SloanM = (457/DCs) - 414.2
        #Método ThorlandM
        suma_plieguest = triceps + subescapular + cresta_iliaca
        DCtm= 1.0987 - 0.00122*suma_plieguest + 0.00000263*(suma_plieguest)**2
        ThorlandM = (495/DCtm) - 450
        porcentaje_grasa = statistics.mean([DurninM, JacksonM, WilmarM, SloanM, ThorlandM])  # Sustituir con la fórmula real
        return porcentaje_grasa



