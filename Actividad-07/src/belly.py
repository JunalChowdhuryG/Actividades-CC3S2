# clase Belly
class Belly:
    # constructor
    def __init__(self, clock_service=None):
        self.pepinos_comidos = 0
        self.tiempo_esperado = 0
        self.clock_service = clock_service  # Puede ser mock

    # metodo resetear el estomago
    def reset(self):
        self.pepinos_comidos = 0
        self.tiempo_esperado = 0

    # metodo comer pepinos
    def comer(self, pepinos):
        if pepinos < 0:
            raise ValueError("La cantidad de pepinos no puede ser negativa.")
        if pepinos > 1000:
            raise ValueError("Demasiados pepinos.")
        self.pepinos_comidos += pepinos

    # metodo esperar
    def esperar(self, horas):
        if horas < 0:
            raise ValueError("El tiempo no puede ser negativo.")
        self.tiempo_esperado += horas

    # metodo para saber si el estomago grune
    def esta_gruniendo(self):
        return self.tiempo_esperado >= 1.5 and self.pepinos_comidos > 10

    # metodo para grunir
    def pepinos_para_gruñir(self):
        if self.pepinos_comidos > 10:
            return 0
        return max(0, 11 - self.pepinos_comidos)

    # metodo para predecir si el estomago grune
    def predecir_gruñido(self, pepinos, horas):
        return horas >= 1.5 and pepinos > 10
