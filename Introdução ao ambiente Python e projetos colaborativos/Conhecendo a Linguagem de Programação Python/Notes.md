# Modo Interativo no Python

O interpretador Python pode executar em modo que possibilite o
desenvolvedor a escrever o código, e ver o resultado de forma imediata.

## Como iniciar ?

### Existe duas formas de abrir o Modo Interativo:

1. Insira o comando abaixo, para chamar apenas o interpretador: 
```bash
python
```

2. Ou execute o script com a flag -i: 
```bash
app.py
```

### Para encerrar a operação do terminal interativo, insira o comando:

```bash
exit()
```

---

# Programas em Python

## Como executar programas ?

1. Para executar um programa, insira o comando seguido do nome do arquivo:

```bash
python ${NAMES_FILE}
```

2. Para executar um programa e abrir o Modo Interativo, relacionado com o arquivo, insira o comando seguido do nome do arquivo:

```bash
python -i ${NAMES_FILE}
```

## Funções

### dir

Sem argumentos, retorna a lista de nomes no escopo local atual. Com um argumento, retorna uma lista de atributos válidos para o objeto.

1. Retornando uma lista de nomes do escopo local atual:

```bash
dir()
```

2. Retornando uma lista de atributos (por exemplo: 100) válidos para o objeto:

```bash
dir(${ATRIBUTE})
```

### help

Invoca o sistema de ajuda integrado. É possível buscar em modo interativo ou informar por parâmetro qual o nome do módulo, função, classe, método ou variável. Exemplo:

1. Retorna uma mensagem sobre a ferramenta de ajuda e abre o "navegador" de pesquisa, insira o comando:

```bash
help()
```

2. Retorna uma mensagem baseada em um pârametro sobre a ferramenta de ajuda e abre o "navegador" de pesquisa, insira o comando:

```bash
help(${ATRIBUTE})
```
# Outros 

## Comentários

1. Utilize "#" para iniciar um comentário
2. Aperte CTRL + {TECLA_COM_:_;}