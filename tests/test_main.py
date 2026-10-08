import string

import pytest

import src.main as cli
from src.generator import TAMANHO_SENHA


def test_gera_senha_padrao_e_retorna_codigo_de_sucesso(capsys):
    exit_code = cli.main([])

    output = capsys.readouterr().out.strip()
    assert exit_code == 0
    assert output.startswith("Senha gerada: ")
    assert len(output.partition(": ")[2]) == TAMANHO_SENHA


def test_gera_senha_com_tamanho_e_todos_os_grupos(capsys):
    exit_code = cli.main(
        [
            "--length",
            "12",
            "--lowercase",
            "--uppercase",
            "--numbers",
            "--symbols",
        ]
    )
    senha = capsys.readouterr().out.strip().partition(": ")[2]

    assert exit_code == 0
    assert len(senha) == 12
    assert any(caractere in string.ascii_lowercase for caractere in senha)
    assert any(caractere in string.ascii_uppercase for caractere in senha)
    assert any(caractere in string.digits for caractere in senha)
    assert any(caractere in string.punctuation for caractere in senha)


def test_aceita_forma_abreviada_e_um_grupo(capsys):
    exit_code = cli.main(["-l", "8", "--uppercase"])
    senha = capsys.readouterr().out.strip().partition(": ")[2]

    assert exit_code == 0
    assert len(senha) == 8
    assert all(caractere in string.ascii_uppercase for caractere in senha)


def test_rejeita_tamanho_menor_que_quantidade_de_grupos(capsys):
    exit_code = cli.main(
        ["--length", "3", "--lowercase", "--uppercase", "--numbers", "--symbols"]
    )

    output = capsys.readouterr().err
    assert exit_code == 1
    assert "tamanho deve ser pelo menos" in output
    assert "Traceback" not in output


def test_exibe_ajuda_e_encerra_com_sucesso(capsys):
    with pytest.raises(SystemExit) as error:
        cli.main(["--help"])

    assert error.value.code == 0
    help_output = capsys.readouterr().out
    assert "--length" in help_output
    assert "--lowercase" in help_output


def test_argumento_desconhecido_exibe_erro_sem_traceback(capsys):
    with pytest.raises(SystemExit) as error:
        cli.main(["--opcao-inexistente"])

    output = capsys.readouterr().err
    assert error.value.code == 2
    assert "error:" in output
    assert "Traceback" not in output


def test_erro_do_core_e_exibido_sem_traceback(monkeypatch, capsys):
    def gerar_senha_com_erro(*args, **kwargs):
        raise ValueError("erro de validação")

    monkeypatch.setattr(cli, "gerar_senha", gerar_senha_com_erro)

    exit_code = cli.main([])

    output = capsys.readouterr().err
    assert exit_code == 1
    assert "Erro ao gerar a senha: erro de validação" in output
    assert "Traceback" not in output
