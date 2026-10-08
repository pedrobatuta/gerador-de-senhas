"""Core do gerador de senhas seguras."""

from .generator import gerar_senha
from .validator import validar_senha

__all__ = ["gerar_senha", "validar_senha"]
