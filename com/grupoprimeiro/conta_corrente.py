class ContaCorrente:

    def __init__(self, numero, nome_correntista, saldo=0.0):
        self.numero = numero
        self.alterar_nome(nome_correntista)
        self.saldo = saldo

    def alterar_nome(self, nome_correntista):
        self.nome_correntista = nome_correntista

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor
