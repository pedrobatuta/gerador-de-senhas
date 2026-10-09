# Gerador de Senhas Seguras

## 1. Descrição

Este MVP em Python gera senhas aleatórias por meio de um único core em `src`.
As interfaces `src.main` e `gerador_senhas.py` permitem configurar tamanho e
grupos de caracteres, mantendo padrões diferentes para compatibilidade.

## 2. Objetivo

O projeto demonstra como organizar um gerador de senhas e documentar seu
desenvolvimento. No contexto acadêmico, aplica arquitetura modular, interface
de linha de comando (CLI), validação de dados, testes automatizados, controle
de versão com Git e documentação.

## 3. Funcionalidades

O projeto contém duas interfaces de terminal que reutilizam o mesmo gerador:

- `src.main` aceita tamanho e grupos por argumentos CLI; sem grupos informados,
  usa minúsculas e números, com tamanho padrão de seis caracteres;
- `gerador_senhas.py` mantém tamanho padrão de 20 e todos os quatro grupos
  habilitados; também permite desativar grupos e excluir caracteres ambíguos;
- o core garante ao menos um caractere de cada grupo selecionado e rejeita
  critérios sem grupos ou com tamanho insuficiente;
- `src.validator` valida senhas conforme o tamanho e os grupos escolhidos;
- o core usa `secrets` para escolher e embaralhar os caracteres.

## 4. Arquitetura e estrutura do projeto

```text
MVP/
├── .gitignore
├── LICENSE
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
├── requirements.txt
└── README.md
```

- `src/main.py`: interpreta os argumentos da CLI, chama o gerador do core e
  apresenta a senha ou uma mensagem de erro.
- `src/generator.py`: implementação única da geração segura; seleciona os
  grupos, garante sua presença e usa `secrets`.
- `src/validator.py`: centraliza os critérios e valida se uma senha atende ao
  tamanho e aos grupos selecionados.
- `tests/`: contém testes pytest para o gerador, o validador e a CLI em `src`.
- `gerador_senhas.py`: interface de terminal compatível que converte suas
  opções para os parâmetros do gerador em `src`.
- `test_gerador_senhas.py`: contém testes `unittest` para o script
  `gerador_senhas.py`.
- `.gitignore`: exclui do Git ambientes virtuais, caches, arquivos temporários
  e outros artefatos locais.
- `LICENSE`: define os termos de uso, cópia, modificação e distribuição do
  projeto sob a licença MIT.
- `requirements.txt`: lista `pytest`, dependência externa usada para executar
  os testes.
- `README.md`: documenta o projeto, suas interfaces e como executar o código e
  os testes.

## 5. Fluxo de dados

O projeto tem dois fluxos de execução:

1. O usuário informa tamanho e grupos em uma das interfaces de terminal.
2. `argparse` interpreta os argumentos e a interface os converte em parâmetros
   do core.
3. A validação em `src.validator` verifica os critérios, incluindo a seleção de
   grupos e o tamanho mínimo necessário.
4. `src.generator` cria a senha usando `secrets` e garante ao menos um
   caractere de cada grupo selecionado.
5. A CLI apresenta a senha ou uma mensagem de erro.

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

5. Instale as dependências listadas em `requirements.txt`:

   ```powershell
   python -m pip install -r requirements.txt
   ```

## 9. Como utilizar

### CLI modular principal

O módulo `src.main` gera por padrão seis caracteres com minúsculas e números.
Use `--help` para ver as opções:

```powershell
python -m src.main --help
```

Gerar uma senha com os quatro grupos e 16 caracteres:

```powershell
python -m src.main --length 16 --lowercase --uppercase --numbers --symbols
```

Usar a forma abreviada `-l` e selecionar apenas letras maiúsculas:

```powershell
python -m src.main -l 12 --uppercase
```

O script `gerador_senhas.py` mantém o padrão de 20 caracteres com
os quatro grupos. Também oferece opções de quantidade e exclusão de caracteres
ambíguos. Use `--help` para ver todas as opções:

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

Os dois comandos reutilizam a geração em `src.generator`. Para executar a
interface modular sem opções, use:

```powershell
python -m src.main
```

Sem flags de grupo, `src.main` usa minúsculas e números. Quando uma ou mais
flags de grupo são informadas, somente os grupos indicados são selecionados.

## 10. Exemplos de saída

Os exemplos abaixo são ilustrativos. Como a senha é aleatória, cada execução
pode produzir um resultado diferente.

Geração pelo módulo `src.main`:

```text
Senha gerada: a3k8q2
```

Erro ao definir tamanho menor que os quatro grupos selecionados em
`gerador_senhas.py`:

```text
gerador_senhas.py: error: O tamanho deve ser pelo menos igual à quantidade de grupos selecionados (4).
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
  verificação dos critérios e de uma senha pronta da lógica de geração.
- Os testes verificam propriedades, como tamanho, caracteres permitidos e
  mensagens, em vez de esperar uma senha específica, pois a saída é aleatória.

## 13. Limitações do MVP

- Não possui interface gráfica.
- Não armazena senhas.
- Não possui integração com banco de dados.
- Não funciona como gerenciador ou cofre de senhas.
- A validação de uma senha pronta é oferecida pelo core, mas as CLIs não pedem
  uma senha existente para validar; elas geram senhas novas.

## 14. Melhorias futuras

- Adicionar um medidor de força da senha.
- Oferecer uma opção para excluir caracteres ambíguos também na interface
  modular.
- Criar uma interface web ou gráfica.
- Permitir configurar quais símbolos podem ser usados.
- Permitir validar uma senha existente por uma das interfaces de terminal.

## 15. Uso da IA generativa

O GitHub Copilot foi utilizado como apoio ao planejamento da estrutura, à
implementação orientada, à criação e revisão de testes e à documentação. O
modelo de linguagem selecionado no Copilot não foi registrado durante o
desenvolvimento e, por isso, não pode ser identificado com confiabilidade.
As sugestões foram revisadas e testadas antes de serem aceitas.

## 16. Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo
[LICENSE](LICENSE) para ver os termos completos.

## 17. Autor

Pedro Egidio Alves de Oliveira
