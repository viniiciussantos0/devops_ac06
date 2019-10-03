import pytest
from com.grupoprimeiro.conta_corrente import ContaCorrente

def test_alterar_nome():
    conta_corrente = ContaCorrente(5, 'lucas')
    conta_corrente.alterarNome('matheus')
    assert conta_corrente.nomeCorrentista == 'matheus'


def test_deposito():
    conta_corrente = ContaCorrente(5, 'lucas', 5)
    conta_corrente.deposito(5)
    assert conta_corrente.saldo == 10


def test_saque():
    conta_corrente = ContaCorrente(5, 'lucas', 5)
    conta_corrente.saque(5)
    assert conta_corrente.saldo == 0
