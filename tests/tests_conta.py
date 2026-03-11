import unittest
from src.models.conta import Conta


class TestConta(unittest.TestCase):

    def test_deposito(self):

        conta = Conta(1000)

        conta.depositar(500)

        self.assertEqual(conta.saldo, 1500)

