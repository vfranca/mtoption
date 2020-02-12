from unittest import TestCase
from mtoptions.estrategia import Estrategia


class TestEstrategia(TestCase):
    def setUp(self):
        self.estrategia = Estrategia()

    def test_obtem_o_nome(self):
        self.assertEqual(self.estrategia.nome, "")

    def test_obtem_a_descricao(self):
        self.assertEqual(self.estrategia.descricao, "")

    def test_obtem_o_que_comprar(self):
        expec = [{"ativo": "call", "tipo": "atm", "volume": 1}]
        self.assertEqual(self.estrategia.compra, expec)

    def test_obtem_o_que_vender(self):
        expec = [{"ativo": "call", "tipo": "atm", "volume": 1}]
        self.assertEqual(self.estrategia.vende, expec)
