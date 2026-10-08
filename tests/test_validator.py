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


def test_valida_senha_com_criterios_configurados():
    assert validar_senha(
        "Ab3!",
        comprimento=4,
        incluir_minusculas=True,
        incluir_maiusculas=True,
        incluir_numeros=True,
        incluir_simbolos=True,
    )


def test_rejeita_senha_sem_um_dos_grupos_selecionados():
    assert not validar_senha(
        "Abc!",
        comprimento=4,
        incluir_minusculas=True,
        incluir_maiusculas=True,
        incluir_numeros=True,
        incluir_simbolos=True,
    )


@pytest.mark.parametrize("senha", ["abcdef", "123456"])
def test_rejeita_senha_sem_letra_minuscula_ou_sem_numero(senha):
    assert not validar_senha(senha)


@pytest.mark.parametrize("senha", ["Abc123", "abc12!", "abc 12"])
def test_rejeita_caracteres_nao_permitidos(senha):
    assert not validar_senha(senha)
