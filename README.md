# Gerador de Senhas Seguras

## 1. Descrição

Este MVP em Python gera senhas aleatórias. O script `gerador_senhas.py` permite
escolher o tamanho e os grupos de caracteres; a interface `src.main` usa as
regras fixas do core em `src`.

## 2. Objetivo

O projeto demonstra como organizar um gerador de senhas e documentar seu
desenvolvimento. No contexto acadêmico, aplica arquitetura modular, interface
de linha de comando (CLI), validação de dados, testes automatizados, controle
de versão com Git e documentação.

## 3. Funcionalidades

O projeto contém duas interfaces de terminal, com funcionalidades diferentes:

- `gerador_senhas.py` permite escolher o tamanho da senha e desativar grupos de
  letras minúsculas, letras maiúsculas, números ou símbolos;
- essa interface garante ao menos um caractere de cada grupo ativo e rejeita a
  seleção sem grupos ou um tamanho menor que a quantidade de grupos ativos;
- `gerador_senhas.py` também permite excluir os caracteres ambíguos `I`, `l`,
  `1`, `O` e `0`;
- `src.main` gera uma senha de seis caracteres, com pelo menos uma letra
  minúscula e um número;
- o módulo `src.validator` verifica se uma senha tem seis caracteres, contém
  somente letras minúsculas e números, e possui ao menos um de cada;
- o gerador em `src` usa o módulo `secrets` para escolher e embaralhar os
  caracteres.

As opções de tamanho e grupos pertencem a `gerador_senhas.py`; elas não são
aceitas por `src.main`.

## 4. Arquitetura e estrutura do projeto

```text
MVP/
├── .vscode/
│   └── settings.json
├── src/
│   ├── __init__.py
│   ├── generator.py
│   ├── main.py
│   └── validator.py
├── tests/
│   ├── __init__.py
│   ├── test_generator.py
│   ├── test_main.py
│   └── test_validator.py
├── gerador_senhas.py
├── test_gerador_senhas.py
└── README.md
```

- `src/main.py`: interpreta os argumentos de `src.main`, chama o gerador do
  core e apresenta a senha ou uma mensagem de erro. Atualmente só aceita a
  ajuda automática `--help`; a geração usa as regras fixas do core.
- `src/generator.py`: gera uma senha de seis caracteres com letras minúsculas
  e números, usando `secrets`.
- `src/validator.py`: verifica se uma senha pronta atende às regras fixas do
  core. Essa função não é chamada por `src.main`.
- `tests/`: contém testes pytest para o gerador, o validador e a CLI em `src`.
- `gerador_senhas.py`: oferece uma segunda interface de terminal com opções
  configuráveis de tamanho e grupos; sua geração e validação estão nesse
  próprio arquivo.
- `test_gerador_senhas.py`: contém testes `unittest` para o script
  `gerador_senhas.py`.
- `.vscode/settings.json`: contém uma configuração local do Visual Studio Code
  para o ambiente Python.
- `.gitignore`: não existe atualmente na raiz do projeto.
- `README.md`: documenta o projeto, suas interfaces e como executar o código e
  os testes.

## 5. Fluxo de dados

O projeto tem dois fluxos de execução:

1. Com `python -m src.main`, o usuário pode pedir ajuda com `--help` ou executar
   a geração padrão. O `argparse` interpreta a linha de comando; a CLI chama
   `src.generator.gerar_senha()` sem argumentos; o core gera a senha e a CLI
   apresenta o resultado. A validação disponível em `src.validator` é
   independente e não participa desse fluxo.
2. Com `python gerador_senhas.py`, o usuário informa tamanho e grupos usando
   as opções próprias desse script. O `argparse` interpreta essas opções; o
   script verifica se há grupos ativos e se o tamanho é suficiente; em seguida
   gera a senha e apresenta o resultado. Erros de configuração são exibidos
   como mensagens da CLI.

## 6. Tecnologias utilizadas

- **Python**: linguagem do projeto.
- **`argparse`, `string` e `secrets`**: módulos da biblioteca padrão do
  Python; não precisam ser instalados separadamente.
- **pytest**: ferramenta externa usada pelos testes da pasta `tests`; precisa
  ser instalada para executá-los.
- **Git**: controle de versão do projeto.
- **Visual Studio Code**: editor usado no desenvolvimento.
- **GitHub Copilot**: apoio ao desenvolvimento.

O teste legado `test_gerador_senhas.py` usa `unittest`, que também faz parte da
biblioteca padrão do Python.

## 7. Pré-requisitos

- Python 3.6 ou superior. O código usa `secrets`, disponível a partir do
  Python 3.6, e f-strings, introduzidas nessa mesma versão.
- Git, para clonar ou versionar o projeto.
- Terminal PowerShell no Windows para os comandos desta documentação.
- pytest para executar os testes localizados em `tests`.

## 8. Instalação no Windows

1. No diretório pai onde deseja criar a pasta do projeto, clone o repositório.
   Substitua `<URL-DO-REPOSITORIO>` pela URL real antes de executar:

   ```powershell
   git clone <URL-DO-REPOSITORIO> MVP
   ```

2. A partir do mesmo diretório pai usado para clonar, entre na pasta do projeto:

   ```powershell
   Set-Location -Path .\MVP
   ```

3. Crie um ambiente virtual:

   ```powershell
   python -m venv .venv
   ```

4. Se a política do PowerShell bloquear scripts, permita a execução somente
   nesta sessão e ative o ambiente:

   ```powershell
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   .\.venv\Scripts\Activate.ps1
   ```

5. Instale pytest. O projeto não possui `requirements.txt`:

   ```powershell
   python -m pip install pytest
   ```

## 9. Como utilizar

### Interface configurável

O script `gerador_senhas.py` gera por padrão uma senha de 20 caracteres com os
quatro grupos. Use `--help` para ver todas as opções:

```powershell
python gerador_senhas.py --help
```

Gerar uma senha com os grupos habilitados por padrão:

```powershell
python gerador_senhas.py
```

Gerar senha apenas com letras minúsculas e números:

```powershell
python gerador_senhas.py --sem-maiusculas --sem-simbolos
```

Usar a forma abreviada `-t` para definir o tamanho:

```powershell
python gerador_senhas.py -t 32
```

Exemplo de entrada inválida: o tamanho 3 é menor do que os quatro grupos
habilitados por padrão:

```powershell
python gerador_senhas.py --tamanho 3
```

Desativar todos os grupos também é inválido:

```powershell
python gerador_senhas.py --sem-minusculas --sem-maiusculas --sem-numeros --sem-simbolos
```

As opções configuráveis são exclusivas de `gerador_senhas.py`. Para executar
a interface modular `src.main`, use:

```powershell
python -m src.main
```

Essa interface gera uma senha segundo as regras fixas do core. A única opção
de linha de comando disponível nela é `--help`.

## 10. Exemplos de saída

Os exemplos abaixo são ilustrativos. Como a senha é aleatória, cada execução
pode produzir um resultado diferente.

Geração pelo módulo `src.main`:

```text
Senha gerada: a3k8q2
```

Erro ao definir tamanho menor que os quatro grupos padrão em
`gerador_senhas.py`:

```text
gerador_senhas.py: error: O comprimento deve ser pelo menos igual ao número de classes selecionadas (4).
```

Erro ao desativar todos os grupos em `gerador_senhas.py`:

```text
gerador_senhas.py: error: Selecione pelo menos uma classe de caracteres.
```

## 11. Como executar os testes

Ative o ambiente virtual e instale pytest antes de executar os testes da pasta
`tests`. Na raiz do projeto:

Executar todos os testes:

```powershell
python -m pytest -q
```

Executar somente os testes do core modular:

```powershell
python -m pytest -q tests\test_generator.py tests\test_validator.py
```

Executar somente os testes da CLI modular:

```powershell
python -m pytest -q tests\test_main.py
```

O teste legado `test_gerador_senhas.py` usa `unittest` e também é descoberto
por pytest.

## 12. Decisões técnicas

- `secrets` é usado para gerar valores imprevisíveis apropriados a senhas;
  `random` é destinado a usos gerais e não a esse propósito.
- A CLI em `src/main.py` fica separada do gerador para manter a interação com
  o terminal fora da implementação do core.
- A validação em `src/validator.py` fica em um módulo próprio para separar a
  verificação de uma senha pronta da sua geração.
- Os testes verificam propriedades, como tamanho, caracteres permitidos e
  mensagens, em vez de esperar uma senha específica, pois a saída é aleatória.

## 13. Limitações do MVP

- Não possui interface gráfica.
- Não armazena senhas.
- Não possui integração com banco de dados.
- Não funciona como gerenciador ou cofre de senhas.
- A interface `src.main` não permite configurar tamanho ou grupos; essa
  configuração está disponível apenas no script `gerador_senhas.py`.
- A validação em `src.validator` não está conectada à execução da CLI modular.

## 14. Melhorias futuras

- Adicionar um medidor de força da senha.
- Oferecer uma opção para excluir caracteres ambíguos também na interface
  modular.
- Criar uma interface web ou gráfica.
- Permitir configurar quais símbolos podem ser usados.
- Unificar as duas interfaces e conectar a validação do core ao fluxo da CLI.

## 15. Uso da IA generativa

O GitHub Copilot foi utilizado como apoio ao planejamento da estrutura, à
implementação orientada, à criação e revisão de testes e à documentação.
As sugestões foram revisadas e testadas antes de serem aceitas.

## 16. Autor

Pedro Egidio Alves de Oliveira
