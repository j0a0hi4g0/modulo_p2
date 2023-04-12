class Conta:
    def __init__(self, agencia, numero):
        self.agencia = agencia
        self.numero = numero
        self.limite = 1000
        self.saldo = 0
        self.historico = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.append(("Depósito", valor))
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if self.saldo + self.limite >= valor > 0:
            self.saldo -= valor
            self.historico.append(("Saque", valor))
        else:
            print("Saldo insuficiente ou valor inválido para saque.")

    def transferir(self, valor, outra_conta):
        if self.saldo >= valor > 0:
            outra_conta.depositar(valor)
            self.saldo -= valor
            self.historico.append(("Transferência", valor))
        else:
            print("Saldo insuficiente ou valor inválido para transferência.")

    def ver_extrato(self):
        print("Extrato da conta {}/{}:".format(self.agencia, self.numero))
        for operacao in self.historico:
            print("{}: R${:.2f}".format(operacao[0], operacao[1]))
        print("Saldo atual: R${:.2f}".format(self.saldo))

    def encerrar_conta(self):
        if self.saldo == 0:
            print("Conta encerrada com sucesso.")
        else:
            print("A conta não pode ser encerrada pois possui saldo positivo.")
