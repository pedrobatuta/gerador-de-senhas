"""Interface configurável de linha de comando do gerador de senhas."""

import argparse

from src.generator import CARACTERES_AMBIGUOS, gerar_senha


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
    except ValueError as error:
        parser.error(str(error))

    print("\n".join(senhas))


if __name__ == "__main__":
    main()
