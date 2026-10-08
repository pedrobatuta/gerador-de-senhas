"""Gerador de senhas seguras para uso no terminal."""

import argparse
import secrets
import string


GRUPOS_CARACTERES = {
    "minusculas": string.ascii_lowercase,
    "maiusculas": string.ascii_uppercase,
    "numeros": string.digits,
    "simbolos": string.punctuation,
}
CARACTERES_AMBIGUOS = "Il1O0"


def gerar_senha(
    comprimento=20,
    incluir_minusculas=True,
    incluir_maiusculas=True,
    incluir_numeros=True,
    incluir_simbolos=True,
    excluir_ambiguos=False,
):
    """Gera uma senha usando o gerador criptograficamente seguro do Python."""
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
            "O comprimento deve ser pelo menos igual ao número de classes selecionadas "
            f"({len(grupos)})."
        )

    senha = [secrets.choice(grupo) for grupo in grupos]
    alfabeto = "".join(grupos)
    senha.extend(
        secrets.choice(alfabeto) for _ in range(comprimento - len(senha))
    )
    secrets.SystemRandom().shuffle(senha)
    return "".join(senha)


def criar_parser():
    parser = argparse.ArgumentParser(
        description="Gera senhas aleatórias usando aleatoriedade criptograficamente segura."
    )
    parser.add_argument(
        "-t",
        "--tamanho",
        type=int,
        default=20,
        help="comprimento de cada senha (padrão: 20)",
    )
    parser.add_argument(
        "-q",
        "--quantidade",
        type=int,
        default=1,
        help="número de senhas a gerar (padrão: 1)",
    )
    parser.add_argument(
        "--sem-minusculas",
        action="store_true",
        help="não incluir letras minúsculas",
    )
    parser.add_argument(
        "--sem-maiusculas",
        action="store_true",
        help="não incluir letras maiúsculas",
    )
    parser.add_argument(
        "--sem-numeros",
        action="store_true",
        help="não incluir números",
    )
    parser.add_argument(
        "--sem-simbolos",
        action="store_true",
        help="não incluir símbolos",
    )
    parser.add_argument(
        "--sem-ambiguos",
        action="store_true",
        help="excluir caracteres visualmente ambíguos (I, l, 1, O e 0)",
    )
    return parser


def main(argv=None):
    parser = criar_parser()
    args = parser.parse_args(argv)

    if args.tamanho < 1:
        parser.error("--tamanho deve ser maior que zero.")
    if args.quantidade < 1:
        parser.error("--quantidade deve ser maior que zero.")

    opcoes = {
        "incluir_minusculas": not args.sem_minusculas,
        "incluir_maiusculas": not args.sem_maiusculas,
        "incluir_numeros": not args.sem_numeros,
        "incluir_simbolos": not args.sem_simbolos,
        "excluir_ambiguos": args.sem_ambiguos,
    }

    try:
        senhas = [
            gerar_senha(args.tamanho, **opcoes) for _ in range(args.quantidade)
        ]
    except ValueError as erro:
        parser.error(str(erro))

    print("\n".join(senhas))


if __name__ == "__main__":
    main()

