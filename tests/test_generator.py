import string

from src.generator import TAMANHO_SENHA, gerar_senha


def test_gera_senha_com_tamanho_padrao():
    senha = gerar_senha()

    assert len(senha) == TAMANHO_SENHA


def test_gera_senha_contem_cada_grupo_selecionado():
    senha = gerar_senha(
        comprimento=12,
        incluir_minusculas=True,
        incluir_maiusculas=True,
        incluir_numeros=True,
        incluir_simbolos=True,
    )

    assert any(caractere in string.ascii_lowercase for caractere in senha)
    assert any(caractere in string.ascii_uppercase for caractere in senha)
    assert any(caractere in string.digits for caractere in senha)
    assert any(caractere in string.punctuation for caractere in senha)


def test_geracoes_consecutivas_normalmente_sao_diferentes():
    primeira_senha = gerar_senha()
    segunda_senha = gerar_senha()

    assert primeira_senha != segunda_senha


def test_gera_senha_com_apenas_um_grupo():
    senha = gerar_senha(
        comprimento=8,
        incluir_minusculas=False,
        incluir_maiusculas=True,
        incluir_numeros=False,
        incluir_simbolos=False,
    )

    assert len(senha) == 8
    assert all(caractere in string.ascii_uppercase for caractere in senha)
