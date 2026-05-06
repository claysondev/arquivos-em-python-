class ContaBancaria: 
    def __init__(self, titular, saldo=0): 
        self.titular = titular 
        self.saldo = saldo 
 
    def depositar(self, valor): 
        if valor > 0: 
            self.saldo += valor 
            print(f"Depósito de R${valor:.2f} realizado com sucesso.") 
        else: 
            print("Valor inválido para depósito.") 
 
    def sacar(self, valor): 
        if valor > self.saldo: 
            print("Saldo insuficiente.") 
        elif valor <= 0: 
            print("Valor inválido para saque.") 
        else: 
            self.saldo -= valor 
            print(f"Saque de R${valor:.2f} realizado com sucesso.") 
 
    def exibir_saldo(self): 
        print(f"Titular: {self.titular}") 
        print(f"Saldo atual: R${self.saldo:.2f}") 
 
# Programa principal 
conta1 = ContaBancaria("Fernando", 1000) 
conta1.exibir_saldo() 
conta1.depositar(500) 
conta1.sacar(300) 
conta1.exibir_saldo()
    