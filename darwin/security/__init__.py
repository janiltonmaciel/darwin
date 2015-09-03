# -*- coding:utf-8 -*-

def unicode_dados(dados):
    if isinstance(dados, unicode):
        dados = dados.encode('utf-8')
    return dados
