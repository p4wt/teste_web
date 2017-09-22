"""
Desenvolva uma calculadora

TDD:
    1 - Escrever para falhar
    2 - Escrever para funcionar
    3 - Refatorar

ATDD:
    1 - Escreva o critério de aceite
    2 - Escrava um código que teste o mesmo
    3 - Refatore o teste
    4 - Refatore o código

BDD:
    1 - Olhe os requisitos
    2 - Entenda os criteŕios de aceite
    3 - Montar as estorias
    4 - Identificar os agentes (usuario, admin, gerente)
    5 - Quais são as ações a serem tomadas pelos agentes


Regra: Transferir dinheiro para contas no exterior (nova funcionalidade)
Criério: Conseguir efetuar transferencias

Estorias:
ator: Eu, como um ["cliente", "gerente", "admin"],
ação: Efetuar uma transferencia
assertiva: Então o valor deve ser debitado da conta do ator
"""
from unittest import TestCase, main
from calc import Calc


class Calculator_tests(TestCase):
    def setUp(self):
        self.calc = Calc()

    def test_soma(self):
        # TDD
        self.assertEqual(self.calc.soma(2, 2), 4)

    def test_soma_de_numeros_inteiros_positivos(self):
        self.assertEqual(self.calc.soma(2, 2), 4)

    def test_soma_de_numeros_inteiros_negativos(self):
        self.assertEqual(self.calc.soma(-2, -2), -4)

main()
