""" Este arquivo contém funções para
    testar as funções do módulo converte_hora """


from com.grupoprimeiro.converte_hora import converte_hora


def test_hora_hora_negativa():
    """ Testa conversão de hora negativa """
    assert converte_hora(-24, 0) is None


def test_hora_minuto_negativo():
    """ Testa conversão de minuto negativa """
    assert converte_hora(0, -5) is None


def test_hora_minuto_positivo_extra():
    """ Testa conversão de minuto positivo extra """
    assert converte_hora(0, 60) is None


def test_hora_hora_positiva_extra():
    """ Testa conversão de hora positivo extra """
    assert converte_hora(24, 0) is None


def test_hora_menor_que_doze():
    """ Testa conversão de hora menor que doze """
    assert converte_hora(11, 0) == '11:00 AM'


def test_hora_zero():
    """ Testa conversão de hora zero """
    assert converte_hora(0, 0) == '12:00 AM'


def test_hora_maior_que_doze():
    """ Testa conversão de hora maior que doze """
    assert converte_hora(13, 0) == '01:00 PM'
