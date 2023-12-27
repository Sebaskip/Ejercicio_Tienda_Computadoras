from ProyectoComputadora.DispositivoEntrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    contadorTeclados = 0

    def __init__(self, tipoEntrada, marca):
        Teclado.contadorTeclados += 1
        super().__init__(tipoEntrada, marca)
        self.idTeclado = Teclado.contadorTeclados

    def __str__(self):
        return f'Teclado Id: {self.idTeclado} = {super().__str__()}'

