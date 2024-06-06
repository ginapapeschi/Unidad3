from ClaseEquipo import Equipo

class Maquinaria(Equipo):
    __tipoMaq: str
    __peso: int

    def __init__(self, marca, model, a, tipo, pot, cap, tarifa, cant, tipoM, peso):
        super().__init__(marca, model, a, tipo, pot, cap, tarifa, cant)
        self.__tipoMaq = tipoM
        self.__peso = peso

    def getTipoMaq(self):
        return self.__tipoMaq
    
    def getPeso(self):
        return self.__peso
    
    def getTarifaAlquiler(self):
        imp = super().getTarifaAlq()
        cantDias= super().getCantDiasAlq()
        if self.getPeso() <= 10:
            imp = imp * cantDias
        elif self.getPeso() > 10:
            imp = imp * cantDias + (cantDias * 20 / 100)
        return imp
