"""Geração de senhas com seis caracteres."""

import secrets
import string


TAMANHO_SENHA = 6
CARACTERES_PERMITIDOS = string.ascii_lowercase + string.digits


def gerar_senha():
    """Gera uma senha de seis caracteres com letras minúsculas e números."""
    senha = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.digits),
    ]
    senha.extend(
        secrets.choice(CARACTERES_PERMITIDOS)
        for _ in range(TAMANHO_SENHA - len(senha))
    )
    secrets.SystemRandom().shuffle(senha)
    return "".join(senha)
