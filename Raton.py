from ProyectoComputadora.DispositivoEntrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    contadorRatones = 0

    def __init__(self, tipoEntrada, marca):
        Raton.contadorRatones += 1
        DispositivoEntrada.__init__(self,tipoEntrada, marca)
        self.idRaton = Raton.contadorRatones


    def __str__(self):
        return f'Raton Id: {self.idRaton} = {DispositivoEntrada.__str__(self)}\n'



