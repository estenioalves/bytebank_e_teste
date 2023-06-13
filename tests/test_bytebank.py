from codigo.bytebank import Funcionario
import pytest
from pytest import mark

class TestClass:
    def test_quando_idade_recebe_19_04_1994_deve_retornar_29(self):

        entrada = "19/04/1994" #Given-Contexto
        esperado = 29

        funcionario_teste = Funcionario('Teste', entrada, 1111) #When - Ação
        resultado = funcionario_teste.idade()

        assert resultado == esperado #Then - Desfecho

    def test_quando_sobrenome_recebe_Estenio_Miquelin_Ribeiro_Alves_deve_retornar_Alves(self):
        entrada = 'Estenio Miquelin Ribeiro Alves'
        esperado = 'Alves'

        estenio = Funcionario(entrada,"19/04/1994", 1111)
        resultado = estenio.sobrenome()

        assert resultado == esperado

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000  # given
        entrada_sobrenome = 'Bragança'
        esperado = 90000


        funcionario_teste = Funcionario(entrada_sobrenome, '19/04/1994', entrada_salario)
        funcionario_teste.decrescimo_salario()  # when
        resultado = funcionario_teste.salario

        assert resultado == esperado  # then

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000  # given
        esperado = 100

        funconario_teste = Funcionario('teste', '11/11/2000', entrada)
        resultado = funconario_teste.calcular_bonus() # when

        assert resultado == esperado  # then

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_100000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 100000000  # given

            funconario_teste = Funcionario('teste', '11/11/2000', entrada)
            resultado = funconario_teste.calcular_bonus()  # when

            assert resultado  # then