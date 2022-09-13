from cuenta import CuentaBancaria
from usuario import Usuario

CarolinaOrellana=Usuario("Carolina Orellana", "carolina@mail.com", 2345)
# print(CarolinaOrellana) #si todo esta bien

CarolinaOrellana.hacer_depósito(2000).hacer_retiro(2200).mostrar_balance_usuario()

CarolinaOrellana.abrir_nueva_cuenta(5555)
print(CarolinaOrellana.mis_cuentas)
print(CarolinaOrellana.cuenta.numero_cuenta)
CarolinaOrellana.mostrar_cuentas_usuario()
CarolinaOrellana.depositar_en_cuenta_especifica(5555, 400)

CarolinaOrellana.mostrar_balance_todas_las_cuentas().retirar_en_cuenta_especifica(2345,800).mostrar_balance_todas_las_cuentas().mostrar_balance_cuenta_especifica(2345).hacer_depósito(20).hacer_retiro(80).mostrar_balance_usuario()

#------------------------Probando en Nuevos usuarios
# Acá si me funcionó mezclar metodos.
print("Nuevo Usuario")

DanielaMontecino = Usuario("Daniela Montecino", "daniela@mail.com", 7878)

DanielaMontecino.mostrar_cuentas_usuario().abrir_nueva_cuenta(1212).mostrar_cuentas_usuario().abrir_nueva_cuenta(9090).depositar_en_cuenta_especifica(7878,100).depositar_en_cuenta_especifica(1212,600).depositar_en_cuenta_especifica(9090,50).mostrar_balance_todas_las_cuentas().hacer_retiro(30).mostrar_balance_usuario()