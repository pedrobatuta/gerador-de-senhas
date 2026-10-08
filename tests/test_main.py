import sys

import pytest

import src.main as cli
from src.generator import TAMANHO_SENHA


def test_gera_senha_e_retorna_codigo_de_sucesso(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["src.main"])

    exit_code = cli.main()

    output = capsys.readouterr().out.strip()
    assert exit_code == 0
    assert output.startswith("Senha gerada: ")
    assert len(output.partition(": ")[2]) == TAMANHO_SENHA


def test_exibe_ajuda_e_encerra_com_sucesso(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["src.main", "--help"])

    with pytest.raises(SystemExit) as error:
        cli.main()

    assert error.value.code == 0
    assert "usage:" in capsys.readouterr().out


def test_argumento_desconhecido_exibe_erro_sem_traceback(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["src.main", "--opcao-inexistente"])

    with pytest.raises(SystemExit) as error:
        cli.main()

    output = capsys.readouterr().err
    assert error.value.code == 2
    assert "error:" in output
    assert "Traceback" not in output


def test_erro_do_core_e_exibido_sem_traceback(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["src.main"])

    def gerar_senha_com_erro():
        raise ValueError("erro de validação")

    monkeypatch.setattr(cli, "gerar_senha", gerar_senha_com_erro)

    exit_code = cli.main()

    output = capsys.readouterr().err
    assert exit_code == 1
    assert "Erro ao gerar a senha: erro de validação" in output
    assert "Traceback" not in output
