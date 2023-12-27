from ProyectoComputadora.Computadora import Computadora
from ProyectoComputadora.Monitor import Monitor
from ProyectoComputadora.Orden import Orden
from ProyectoComputadora.Raton import Raton
from ProyectoComputadora.Teclado import Teclado

tec1 = Teclado('USB', 'Accer')
rat1 = Raton('Tipo C', 'Lenovo')
mon1 = Monitor('Hp', '15 Pulgadas')
comp1 = Computadora('Pavilion',mon1,tec1,rat1)

tec2 = Teclado('USB', 'Asus')
rat2 = Raton('Tipo A', 'Casio')
mon2 = Monitor('LG', '12 Pulgadas')
comp2 = Computadora('Gaming RT',mon2,tec2,rat2)

tec3 = Teclado('Bluetooth', 'Hp')
rat3 = Raton('USB', 'LG')
comp3 = Computadora('Familiar', mon2, tec3, rat1)

computadoras1 = [comp1,comp2]
orden1 = Orden(computadoras1)
print(orden1)
orden1.agregarComputadora(comp3)
print(orden1)

computadoras2 = [comp1, tec3, rat1]
orden2 = Orden(computadoras2)
print(orden2)