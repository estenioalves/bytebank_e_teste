from codigo.bytebank import Funcionario

def test_idade():
    funcionario_teste = Funcionario('teste', '19/04/1994', 1111)
    print(f'Teste= {funcionario_teste.idade()}')

test_idade()
