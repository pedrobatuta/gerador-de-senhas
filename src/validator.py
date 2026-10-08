"""Validação das regras de uma senha."""

import string

from .generator import CARACTERES_PERMITIDOS, TAMANHO_SENHA


def validar_senha(senha):
    """Retorna se a senha segue o tamanho, os caracteres e as classes exigidas."""
    if not isinstance(senha, str) or len(senha) != TAMANHO_SENHA:
        return False

    if any(caractere not in CARACTERES_PERMITIDOS for caractere in senha):
        return False

    return (
        any(caractere in string.ascii_lowercase for caractere in senha)
        and any(caractere in string.digits for caractere in senha)
    )
