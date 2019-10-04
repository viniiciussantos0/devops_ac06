""" Este arquivo contém funções para
    testar as funções do módulo ContaCorrente """


from com.grupoprimeiro.conta_corrente import ContaCorrente


def test_alterar_nome():
    """ Testa alteração de nome do correntista """
    conta_corrente = ContaCorrente(5, 'lucas')
    conta_corrente.alterar_nome('matheus')
    assert conta_corrente.nome_correntista == 'matheus'


def test_deposito():
    """ Testa depósito na conta """
    conta_corrente = ContaCorrente(5, 'lucas', 5)
    conta_corrente.deposito(5)
    assert conta_corrente.saldo == 10


def test_saque():
    """ Testa o saque na conta """
    conta_corrente = ContaCorrente(5, 'lucas', 5)
    conta_corrente.saque(5)
    assert conta_corrente.saldo == 0
