"""
Classes das estratégias
"""


class Estrategia(object):
    """Classe base para uma estratégia."""

    nome = ""

    descricao = ""

    compra = [{"ativo": "call", "tipo": "atm", "volume": 1}]

    vende = [{"ativo": "call", "tipo": "atm", "volume": 1}]
