class ContaCorrente:

    def __init__(self, numero, nome_correntista, saldo=0.0):
        """ Construtor da classe Conta Corrente """
        self.numero = numero
        self.alterar_nome(nome_correntista)
        self.saldo = saldo

    def alterar_nome(self, nome_correntista):
        """ Altera o nome do correntista """
        self.nome_correntista = nome_correntista

    def deposito(self, valor):
        """ Insere valor do depósito no saldo """
        self.saldo += valor

    def saque(self, valor):
        """ Desconta o valor do saque no saldo """
        self.saldo -= valor
