def valor_pagamento(valor, dias_atraso):

    if valor < 0:
        return None
    if dias_atraso > 0:
        multa = valor * 0.03
        adicional_atraso = valor * (dias_atraso * 0.01)
        return valor + multa + adicional_atraso
    
    return valor
