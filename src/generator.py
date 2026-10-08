"""Geração segura de senhas."""

import secrets

from .validator import (
    CARACTERES_AMBIGUOS,
    GRUPOS_CARACTERES,
    TAMANHO_SENHA,
    validar_criterios,
)

CARACTERES_PERMITIDOS = (
    GRUPOS_CARACTERES["minusculas"] + GRUPOS_CARACTERES["numeros"]
)


def gerar_senha(
    comprimento=TAMANHO_SENHA,
    incluir_minusculas=True,
    incluir_maiusculas=False,
    incluir_numeros=True,
    incluir_simbolos=False,
    excluir_ambiguos=False,
):
    """Gera uma senha com ao menos um caractere de cada grupo ativo."""
    grupos = validar_criterios(
        comprimento,
        incluir_minusculas=incluir_minusculas,
        incluir_maiusculas=incluir_maiusculas,
        incluir_numeros=incluir_numeros,
        incluir_simbolos=incluir_simbolos,
        excluir_ambiguos=excluir_ambiguos,
    )

    senha = [secrets.choice(grupo) for grupo in grupos]
    alfabeto = "".join(grupos)
    senha.extend(
        secrets.choice(alfabeto) for _ in range(comprimento - len(senha))
    )
    secrets.SystemRandom().shuffle(senha)
    return "".join(senha)
