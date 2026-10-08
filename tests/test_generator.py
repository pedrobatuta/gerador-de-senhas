import string

from src.generator import CARACTERES_PERMITIDOS, TAMANHO_SENHA, gerar_senha


def test_gera_senha_com_tamanho_configurado():
    senha = gerar_senha()

    assert len(senha) == TAMANHO_SENHA


def test_gera_senha_com_letra_minuscula():
    senha = gerar_senha()

    assert any(caractere in string.ascii_lowercase for caractere in senha)


def test_gera_senha_com_numero():
    senha = gerar_senha()

    assert any(caractere in string.digits for caractere in senha)


def test_gera_senha_somente_com_caracteres_permitidos():
    senha = gerar_senha()

    assert all(caractere in CARACTERES_PERMITIDOS for caractere in senha)


def test_geracoes_consecutivas_normalmente_sao_diferentes():
    primeira_senha = gerar_senha()
    segunda_senha = gerar_senha()

    assert primeira_senha != segunda_senha
