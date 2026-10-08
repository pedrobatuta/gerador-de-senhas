"""Validação dos critérios e das senhas geradas."""

import string


TAMANHO_SENHA = 6
CARACTERES_AMBIGUOS = "Il1O0"
GRUPOS_CARACTERES = {
    "minusculas": string.ascii_lowercase,
    "maiusculas": string.ascii_uppercase,
    "numeros": string.digits,
    "simbolos": string.punctuation,
}


def validar_criterios(
    comprimento,
    incluir_minusculas=True,
    incluir_maiusculas=False,
    incluir_numeros=True,
    incluir_simbolos=False,
    excluir_ambiguos=False,
):
    """Retorna os grupos ativos ou informa por que os critérios são inválidos."""
    if not isinstance(comprimento, int) or isinstance(comprimento, bool):
        raise ValueError("O tamanho deve ser um número inteiro.")

    if comprimento < 1:
        raise ValueError("O tamanho deve ser maior que zero.")

    opcoes = {
        "minusculas": incluir_minusculas,
        "maiusculas": incluir_maiusculas,
        "numeros": incluir_numeros,
        "simbolos": incluir_simbolos,
    }
    grupos = []

    for nome, incluir in opcoes.items():
        if incluir:
            grupo = GRUPOS_CARACTERES[nome]
            if excluir_ambiguos:
                grupo = "".join(
                    caractere
                    for caractere in grupo
                    if caractere not in CARACTERES_AMBIGUOS
                )
            grupos.append(grupo)

    if not grupos:
        raise ValueError("Selecione pelo menos uma classe de caracteres.")

    if comprimento < len(grupos):
        raise ValueError(
            "O tamanho deve ser pelo menos igual à quantidade de grupos selecionados "
            f"({len(grupos)})."
        )

    return grupos


def validar_senha(
    senha,
    comprimento=TAMANHO_SENHA,
    incluir_minusculas=True,
    incluir_maiusculas=False,
    incluir_numeros=True,
    incluir_simbolos=False,
    excluir_ambiguos=False,
):
    """Retorna se a senha atende ao tamanho e aos grupos selecionados."""
    if not isinstance(senha, str):
        return False

    try:
        grupos = validar_criterios(
            comprimento,
            incluir_minusculas=incluir_minusculas,
            incluir_maiusculas=incluir_maiusculas,
            incluir_numeros=incluir_numeros,
            incluir_simbolos=incluir_simbolos,
            excluir_ambiguos=excluir_ambiguos,
        )
    except ValueError:
        return False

    if len(senha) != comprimento:
        return False

    caracteres_permitidos = "".join(grupos)
    if any(caractere not in caracteres_permitidos for caractere in senha):
        return False

    return all(any(caractere in grupo for caractere in senha) for grupo in grupos)
