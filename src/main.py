"""Interface de linha de comando do gerador de senhas."""

import argparse
import sys

from .generator import TAMANHO_SENHA, gerar_senha


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Gera uma senha segura conforme o tamanho e os grupos escolhidos."
    )
    parser.add_argument(
        "-l",
        "--length",
        type=int,
        default=TAMANHO_SENHA,
        help=f"tamanho da senha (padrão: {TAMANHO_SENHA})",
    )
    parser.add_argument(
        "--lowercase",
        action="store_true",
        help="incluir letras minúsculas",
    )
    parser.add_argument(
        "--uppercase",
        action="store_true",
        help="incluir letras maiúsculas",
    )
    parser.add_argument(
        "--numbers",
        action="store_true",
        help="incluir números",
    )
    parser.add_argument(
        "--symbols",
        action="store_true",
        help="incluir símbolos",
    )
    args = parser.parse_args(argv)

    grupos_selecionados = any(
        (args.lowercase, args.uppercase, args.numbers, args.symbols)
    )
    opcoes = {
        "incluir_minusculas": args.lowercase if grupos_selecionados else True,
        "incluir_maiusculas": args.uppercase,
        "incluir_numeros": args.numbers if grupos_selecionados else True,
        "incluir_simbolos": args.symbols,
    }

    try:
        password = gerar_senha(args.length, **opcoes)
    except ValueError as error:
        print(f"Erro ao gerar a senha: {error}", file=sys.stderr)
        return 1

    print(f"Senha gerada: {password}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
