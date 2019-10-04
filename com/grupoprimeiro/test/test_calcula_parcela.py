from com.grupoprimeiro.calcula_parcela import valor_pagamento


def test_valor_pagamento_sem_atraso():
    """ Testa valor pagamento sem atraso """
    assert valor_pagamento(20, 0) == 20


def test_valor_pagamento_com_atraso():
    """ Testa valor pagamento com atraso """
    assert valor_pagamento(20, 2) == 21


def test_valor_pagament_sem_valor():
    """ Testa valor pagamento sem valor """
    assert valor_pagamento(-5, 0) is None
