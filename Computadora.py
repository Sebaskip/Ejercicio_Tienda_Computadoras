from Monitor import Monitor
from Raton import Raton
from Teclado import Teclado


class Computadora():
    contadorComputadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contadorComputadoras += 1
        self.idComputadora = Computadora.contadorComputadoras
        self._nombre = nombre
        self.monitor = monitor
        self.teclado = teclado
        self.raton = raton

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    def __str__(self):
        return f'''
Computadora Id: {self.idComputadora} = Nombre: {self._nombre}
Monitor {self.monitor}
Teclado: {self.teclado}
Raton: {self.raton}
        '''


if __name__ == '__main__':
    moni = Monitor('Asus', 'Pequeño')
    tec = Teclado('Usb', 'Lenovo')
    rat = Raton('Cable', 'Hp')
    obj = Computadora('Pavilion', moni, tec, rat)
    print(obj)
