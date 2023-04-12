class Conta:
    def __init__(self, agencia, numero, limite=1000):
        self.agencia = agencia
        self.numero = numero
        self.limite = limite
        self.saldo = 0
        self.historico = []

    def autenticar(self, senha):
        # Implementação da autenticação do usuário
        pass

    def validar_valor(self, valor):
        if valor <= 0:
            raise ValueError('O valor deve ser positivo')
        if valor > self.saldo + self.limite:
            raise ValueError('Saldo insuficiente')

    def depositar(self, valor):
        self.validar_valor(valor)
        self.saldo += valor
        self.historico.append({'tipo': 'Depósito', 'valor': valor})

    def sacar(self, valor):
        self.validar_valor(valor)
        if valor > self.saldo:
            raise ValueError('Saldo insuficiente')
        self.saldo -= valor
        self.historico.append({'tipo': 'Saque', 'valor': valor})

    def transferir(self, conta_destino, valor):
        self.validar_valor(valor)
        if valor > self.saldo:
            raise ValueError('Saldo insuficiente')
        conta_destino.depositar(valor)
        self.saldo -= valor
        self.historico.append({'tipo': 'Transferência', 'valor': valor, 'conta_destino': conta_destino.numero})

    def configurar_limite(self, limite):
        self.limite = limite

    def configurar_notificacoes(self, email):
        # Implementação da configuração de notificações
        pass

    def integrar_servico(self, servico):
        # Implementação da integração com outros serviços
        pass

    def consultar_saldo(self):
        return self.saldo

    def consultar_extrato(self):
        return self.historico

    def encerrar_conta(self):
        # Implementação do encerramento da conta
        pass
