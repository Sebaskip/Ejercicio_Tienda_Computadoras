class Monitor:
    contadorMonitores = 0

    def __init__(self, marca, tamano):
        Monitor.contadorMonitores += 1
        self.idMonitor = Monitor.contadorMonitores
        self._marca = marca
        self._tamano = tamano

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def tamano(self):
        return self._tamano

    @tamano.setter
    def tamano(self, tamano):
        self._tamano = tamano

    def __str__(self):
        return f'ID: {self.idMonitor} = Marca: {self._marca} - Tamaño: {self._tamano}'

