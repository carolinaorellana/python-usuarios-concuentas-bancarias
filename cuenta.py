#Crea una clase CuentaBancaria con los atributos tasa de interés y balance
class CuentaBancaria:
    #ATRIBUTOS
    todas_las_cuentas = []
    #parametros predeterminados 
    def __init__ (self,numero_cuenta, balance=0,tasa_interes=0.01):
        self.numero_cuenta= numero_cuenta
        self.balance = balance
        self.tasa_interes= tasa_interes
        CuentaBancaria.todas_las_cuentas.append(self)

    # Agrega un método depósito a la clase CuentaBancaria:
    def deposito(self,monto):
        self.balance += monto
        return self

    #Agrega un método retiro a la clase CuentaBancaria:
    def retiro(self,monto):
        if self.balance>monto:
            self.balance -= monto
        else:
            print (f"Fondos insuficientes: cobrando una tarifa de $5")
            self.balance -= 5
        return self

    #Agrega un método mostrar_info_cuenta a la clase CuentaBancaria
    def mostrar_info_cuenta (self):
        print(f"Balance: {self.balance}")
        return self

    #Agrega un método generar_interés a la clase CuentaBancaria
    def generar_intereses(self):
        if self.balance>0:
            self.balance += self.balance*self.tasa_interes
        return self
    
    #BONUS NINJA: utiliza un método de clase para imprimir todas las instancias de la información de una cuenta bancaria
    @classmethod
    def imprimir_todas_las_cuentas(cls):
        #print(cls.todas_las_cuentas)
        for cuenta in cls.todas_las_cuentas:
            #print (cuenta.balance)
            #print (cuenta.__dict__)
            print (f"Esta cuenta tiene un balance de {cuenta.balance}")
        #return (f"Hay un total de {len(cls.todas_las_cuentas)} cuentas")
        #sin el return me da none a la hora de llamar a la función)
    
    @classmethod
    def suma_todos_los_balances(cls):
        sum = 0
        # utilizamos cls para referirnos a la clase 
        for cuenta in cls.todas_las_cuentas:
            sum += cuenta.balance
        return sum
