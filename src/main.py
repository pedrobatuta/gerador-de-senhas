"""Interface de linha de comando do gerador de senhas."""

import argparse
import sys

from .generator import gerar_senha


def main():
    parser = argparse.ArgumentParser(
        description="Gera uma senha segura com as regras atuais do core."
    )
    parser.parse_args()

    try:
        password = gerar_senha()
    except ValueError as error:
        print(f"Erro ao gerar a senha: {error}", file=sys.stderr)
        return 1

    print(f"Senha gerada: {password}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
