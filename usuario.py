from cuenta import CuentaBancaria

class Usuario:    
    def __init__(self, nombre, correo,numero_cuenta):
        self.nombre = nombre
        self.correo = correo
        self.mis_cuentas= []
        self.cuenta = CuentaBancaria(numero_cuenta, balance=0,tasa_interes=0.02) #se añade una instancia de cuentaBancaria a la clase usuario
        self.mis_cuentas.append(self.cuenta)
    
    #Metodos relacionados a la creación de nuevas cuentas:
    def abrir_nueva_cuenta(self, numero_cuenta):
        nueva_cuenta=CuentaBancaria(numero_cuenta, balance=0,tasa_interes=0.02)
        self.mis_cuentas.append(nueva_cuenta)
        return self

    def mostrar_cuentas_usuario(self):
        for cuenta in self.mis_cuentas:
            print(f"{cuenta} es la cuenta numero {cuenta.numero_cuenta}")
        return self
    
    def mostrar_balance_todas_las_cuentas(self):
        for cuenta in self.mis_cuentas:
            print(f"La cuenta {cuenta.numero_cuenta} de {self.nombre} tiene un balance de {cuenta.balance}")
        return self

    def depositar_en_cuenta_especifica(self,numero, monto):
        for cuenta in self.mis_cuentas:
            if cuenta.numero_cuenta == numero:
                cuenta.deposito(monto)
        return self

    def retirar_en_cuenta_especifica(self,numero, monto):
        for cuenta in self.mis_cuentas:
            if cuenta.numero_cuenta == numero:
                cuenta.retiro(monto)
        return self

    def mostrar_balance_cuenta_especifica(self,numero):
        for cuenta in self.mis_cuentas:
            if cuenta.numero_cuenta == numero:
                print(f"La cuenta {cuenta.numero_cuenta} de {self.nombre} tiene un balance de {cuenta.balance}")
        return self

    #Metodos relacionados a ver la cuenta por defecto, probar si funcionan también luego de las ediciones de código
    def hacer_depósito(self, monto):
        self.cuenta.deposito(monto)
        return self
    
    def hacer_retiro(self, monto):
        self.cuenta.retiro(monto)
        return self
    
    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.nombre}")
        self.cuenta.mostrar_info_cuenta()
        #Dos maneras de hacerlo
        print(f"Usuario: {self.nombre}, Balance: {self.cuenta.balance}")
        return self 