import pytest

from src.validator import validar_senha


@pytest.mark.parametrize("senha", ["abc12", "abc1234"])
def test_rejeita_senha_com_tamanho_incorreto(senha):
    assert not validar_senha(senha)


@pytest.mark.parametrize("senha", [None, 123456])
def test_rejeita_valor_que_nao_e_texto(senha):
    assert not validar_senha(senha)


def test_aceita_senha_com_letras_minusculas_e_numeros():
    assert validar_senha("abc123")


@pytest.mark.parametrize("senha", ["abcdef", "123456"])
def test_rejeita_senha_sem_letra_minuscula_ou_sem_numero(senha):
    assert not validar_senha(senha)


@pytest.mark.parametrize("senha", ["Abc123", "abc12!", "abc 12"])
def test_rejeita_caracteres_nao_permitidos(senha):
    assert not validar_senha(senha)
