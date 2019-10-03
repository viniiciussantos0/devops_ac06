import pytest
from com.grupoprimeiro.converte_hora import converteHora

def test_hora_hora_negativa():
    assert converteHora(-24, 0) == None


def test_hora_minuto_negativo():
    assert converteHora(0, -5) == None


def test_hora_minuto_positivo_extra():
    assert converteHora(0, 60) == None


def test_hora_hora_positiva_extra():
    assert converteHora(24, 0) == None


def test_hora_menor_que_doze():
    assert converteHora(11, 0) == '11:00 AM'
    

def test_hora_zero():
    assert converteHora(0, 0) == '12:00 AM'
    

def test_hora_maior_que_doze():
    assert converteHora(13, 0) == '01:00 PM'

    