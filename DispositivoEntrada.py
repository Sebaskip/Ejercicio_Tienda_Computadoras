class DispositivoEntrada:
    def __init__(self, tipoEntrada, marca):
        self._tipoEntrada = tipoEntrada
        self._marca = marca

    @property
    def tipoentrada(self):
        return self._tipoEntrada

    @tipoentrada.setter
    def tipoentrada(self, tipoEntrada):
        self._tipoEntrada = tipoEntrada

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    def __str__(self):
        return f'Tipo de entrada: {self._tipoEntrada} - Marca: {self._marca}'
