# Gerador de senhas seguras

Um gerador de senhas simples para terminal, feito com a biblioteca padrão do
Python. As senhas usam `secrets`, apropriado para gerar valores imprevisíveis.

## Requisitos

- Python 3.8 ou superior

## Uso

Gere uma senha de 20 caracteres (padrão):

```powershell
python gerador_senhas.py
```

Defina o tamanho e gere mais de uma senha:

```powershell
python gerador_senhas.py --tamanho 32 --quantidade 5
```

Desabilite classes de caracteres ou remova caracteres ambíguos:

```powershell
python gerador_senhas.py --sem-simbolos --sem-ambiguos
```

As opções `--sem-minusculas`, `--sem-maiusculas`, `--sem-numeros` e
`--sem-simbolos` podem ser combinadas. Pelo menos uma classe deve permanecer
ativa, e o tamanho precisa comportar ao menos um caractere de cada classe ativa.

## Testes

```powershell
python -m unittest
```
