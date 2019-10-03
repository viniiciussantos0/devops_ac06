import pytest
from com.grupoprimeiro.calcula_parcela import valorPagamento

def test_valor_pagamento_sem_atraso():
    assert valorPagamento(20, 0) == 20


def test_valor_pagamento_com_atraso():
    assert valorPagamento(20, 2) == 21


def test_valor_pagament_sem_valor():
    assert valorPagamento(-5, 0) == None