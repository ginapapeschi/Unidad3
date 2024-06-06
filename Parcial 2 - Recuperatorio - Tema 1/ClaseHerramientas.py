from ClaseEquipo import Equipo

class Herramienta(Equipo):
    __herramienta: str

    def __init__(self, marca, model, a, tipo, pot, cap, tarifa, cant, h):
        super().__init__(marca, model, a, tipo, pot, cap, tarifa, cant)
        self.__herramienta = h

    def getHerramienta(self):
        return self.__herramienta

    def getTarifaAlquiler(self):
        imp = super().getTarifaAlq()
        cantDias= super().getCantDiasAlq()
        if self.getHerramienta() == "bateria":
            imp = imp * cantDias + (cantDias * 10 / 100)
        elif self.getHerramienta() == "cable":
            imp = imp * cantDias
        return imp