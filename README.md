# SUSOptiLine
GRUPO 11, González, Gabriel; André, Vinicius.
ILUM ESCOLA DE CIENCIA, CAMPINAS 2024.
## Problemática

O Sistema Único de Saúde (SUS) é um dos maiores e mais complexos sistemas de saúde pública do mundo, responsável por fornecer atendimento médico a milhões de brasileiros. No entanto, um dos problemas mais persistentes e preocupantes que afetam o SUS é a longa espera e a demora no pronto atendimento . As filas nos hospitais e postos de saúde se tornaram uma imagem comum, refletindo a sobrecarga dos serviços de saúde, a falta de recursos e a gestão ineficiente. Este cenário resulta em atrasos críticos no diagnóstico e tratamento, impactando negativamente a saúde e a qualidade de vida dos pacientes.

Pensando nisso, em nosso trabalho final de algoritmos genéticos, decidimos desenvolver um algoritmo genético para otimizar filas de espera no Sistema Único de Saúde (SUS) do Brasil, considerando fatores como idade, gênero e comorbidades para priorização de atendimento.

Contribuições e feedbacks são bem-vindos.

## SUSOptiLine
![MioCard (3)](https://github.com/vinicius-aolm/SUSOptiLine/assets/135054073/7b660a6b-496f-4935-9502-bba2137cf785)
Contribuições e feedbacks são bem-vindos.

# Organização do GIT.
- Readme: Resumo e visão geral do projeto.
- Notebook: `SUSOptiline.ipynb`
- Banco de dados: `Pacientes.csv`

O banco de dados apresenta 150 pacientes hipotéticos, criados pela própria equipe, organizados por ID, idade, gênero e comorbidades. Esses dados também estão disponíveis no notebook SUSOptiLine.ipynb em forma de lista de dicionário.

# Glossário de Funções

Disponíveis em **`funçoes.py`**.

- **criar_gene:** Gera um gene (indivíduo) representando uma possível organização da fila.
- **cria_populacao:** Cria a população inicial de indivíduos.
- **calcular_aptidao:** Calcula a aptidão de um indivíduo com base nos critérios definidos (idade, comorbidades, gênero e posição na fila).
- **funcao_objetivo_pop:** Calcula a aptidão de toda a população.
- **selecao_torneio:** Seleciona indivíduos para reprodução com base em um torneio.
- **cruzamento_ponto_simples:** Realiza o cruzamento de dois indivíduos para gerar novos indivíduos.
- **mutacao_troca:** Aplica mutações aos indivíduos para introduzir variação genética.

# Construção do Algoritmo
### 1. Parâmetros do Algoritmo Genético
Os principais parâmetros do algoritmo genético são:

- **Tamanho da População**: Número de possíveis soluções (indivíduos) em cada geração.
- **Número de Gerações**: Quantidade de iterações que o algoritmo vai executar.
- **Chance de Cruzamento**: Probabilidade de que dois indivíduos se cruzem para formar novos indivíduos.
- **Chance de Mutação**: Probabilidade de que um indivíduo sofra uma mutação.

Vamos começar definindo esses parâmetros:
```python
# Parâmetros do algoritmo
TAMANHO_POPULACAO = 100
NUM_GERACOES = 500
CHANCE_DE_CRUZAMENTO = 0.7
CHANCE_DE_MUTACAO = 0.01
 ```

### 2.Dados dos Pacientes

Vamos definir uma lista de pacientes com suas características:

```python
PACIENTES = [
    {"id": 1, "idade": 70, "genero": "F", "comorbidades": 3},
    {"id": 2, "idade": 65, "genero": "M", "comorbidades": 2},
    {"id": 3, "idade": 45, "genero": "F", "comorbidades": 3},
    {"id": 4, "idade": 46, "genero": "M", "comorbidades": 0},
    {"id": 5, "idade": 50, "genero": "M", "comorbidades": 1},
    {"id": 6, "idade": 80, "genero": "F", "comorbidades": 4},
    {"id": 7, "idade": 55, "genero": "M", "comorbidades": 0},
    {"id": 8, "idade": 60, "genero": "F", "comorbidades": 2},
    {"id": 9, "idade": 65, "genero": "M", "comorbidades": 3},
    {"id": 10, "idade": 70, "genero": "F", "comorbidades": 1},
    {"id": 11, "idade": 75, "genero": "M", "comorbidades": 2},
]
```
### 3.Função para Criar um Gene

Um gene representa uma possível solução (ordem de atendimento dos pacientes). Vamos definir uma função que cria um gene, embaralhando a lista de pacientes:
```python
import random

def criar_gene(pacientes):
    """
    Cria um gene (uma ordem de pacientes).
    
    Args:
        pacientes (list): Lista de dicionários representando os pacientes.
    
    Returns:
        list: Lista embaralhada de pacientes.
    """
    gene = pacientes[:]  # Cópia superficial para preservar a lista original
    random.shuffle(gene)  # Embaralha a ordem dos pacientes
    return gene
```

### 4.Função para Criar a População Inicial

A população inicial é composta por vários genes. Vamos definir uma função que cria uma população inicial:
```python
def cria_populacao(tamanho_populacao, pacientes):
    """
    Cria uma população inicial de genes.
    
    Args:
        tamanho_populacao (int): Número de genes na população.
        pacientes (list): Lista de dicionários representando os pacientes.
    
    Returns:
        list: Lista de genes (população).
    """
    return [criar_gene(pacientes) for _ in range(tamanho_populacao)]
```

### 5.Função de Aptidão

A função de aptidão avalia a qualidade de um gene (uma ordem de pacientes). Vamos definir uma função que calcula a aptidão de uma ordem de pacientes:

```python
def calcular_aptidao(ordem):
    """
    Calcula a aptidão de uma ordem de pacientes.
    
    Args:
        ordem (list): Lista de dicionários representando a ordem dos pacientes.
    
    Returns:
        float: Valor da aptidão calculada.
    """
    aptidao = 0
    for i, paciente in enumerate(ordem):
        peso_idade = 0.8
        peso_genero = 0.5 if paciente["genero"] == "F" else 0.3
        peso_comorbidades = 3.0
        score = (peso_idade * paciente["idade"] +
                 peso_genero +
                 peso_comorbidades * paciente["comorbidades"])
        aptidao += score / (i + 1)
    return aptidao
```

### 6.Função Objetivo para a População
Vamos definir uma função que calcula a aptidão de toda a população:
```python
def funcao_objetivo_pop(populacao):
    """
    Calcula a aptidão para toda a população.
    
    Args:
        populacao (list): Lista de genes (população).
    
    Returns:
        list: Lista de valores de aptidão para cada gene.
    """
    return [calcular_aptidao(gene) for gene in populacao]
```

### 7.Seleção por Torneio

A seleção por torneio é uma técnica onde um número fixo de indivíduos é selecionado aleatoriamente, e o melhor entre eles é escolhido.
Vamos implementar a função de seleção por torneio:
```python
def selecao_torneio(populacao, fitness, tamanho_torneio=3):
    """
    Seleciona indivíduos da população usando o método de torneio.
    
    Args:
        populacao (list): Lista de genes (população).
        fitness (list): Lista de valores de aptidão para cada gene.
        tamanho_torneio (int, optional): Número de competidores em cada torneio. Default é 3.
    
    Returns:
        list: Lista de genes selecionados.
    """
    selecionados = []
    for _ in range(len(populacao)):
        competidores = random.sample(list(zip(populacao, fitness)), tamanho_torneio)
        vencedor = max(competidores, key=lambda x: x[1])
        selecionados.append(vencedor[0])
    return selecionados
```
 ### Diferença entre Seleção por Torneio e Roleta
 - **Seleção por Torneio**: Indivíduos competem em pequenos torneios e o melhor de cada torneio é selecionado. É simples e eficaz, especialmente quando há grande variabilidade na aptidão.
 - **Seleção por Roleta**: Indivíduos são selecionados com probabilidade proporcional à sua aptidão. É menos eficiente quando há pouca diferença na aptidão dos indivíduos.

#### Optamos por usar seleção por torneio porque é mais robusta em cenários onde há grande variabilidade na aptidão, garantindo que os melhores indivíduos sejam frequentemente selecionados.

### 8.Cruzamento de Ponto Simples

O cruzamento combina partes de dois genes para criar novos genes. Vamos implementar uma função para cruzamento de ponto simples:
```python
def cruzamento_ponto_simples(pai, mae, chance_de_cruzamento):
    """
    Realiza o cruzamento de dois genes usando ponto simples.
    
    Args:
        pai (list): Gene pai.
        mae (list): Gene mãe.
        chance_de_cruzamento (float): Probabilidade de realizar o cruzamento.
    
    Returns:
        tuple: Dois novos genes resultantes do cruzamento.
    """
    if random.random() < chance_de_cruzamento:
        ponto = random.randint(1, len(pai) - 1)
        filho1 = pai[:ponto] + [x for x in mae if x not in pai[:ponto]]
        filho2 = mae[:ponto] + [x for x in pai if x not in mae[:ponto]]
        return filho1, filho2
    return pai, mae
```

### 9. Mutação
A mutação altera aleatoriamente um gene para introduzir variabilidade. Vamos implementar uma função de mutação por troca:
```python
def mutacao_troca(individuo, chance_de_mutacao):
    """
    Aplica mutação por troca em um gene.
    
    Args:
        individuo (list): Gene a ser mutado.
        chance_de_mutacao (float): Probabilidade de realizar a mutação.
    
    Returns:
        None
    """
    for i in range(len(individuo)):
        if random.random() < chance_de_mutacao:
            j = random.randint(0, len(individuo) - 1)
            individuo[i], individuo[j] = individuo[j], individuo[i]
```

### 10.Algoritmo Genético
Agora vamos juntar todas as partes e implementar o algoritmo genético completo:

```python
def algoritmo_genetico(pacientes):
    """
    Executa o algoritmo genético para otimizar a ordem de atendimento dos pacientes.
    
    Args:
        pacientes (list): Lista de dicionários representando os pacientes.
    
    Returns:
        tuple: Melhor indivíduo observado e seu valor de aptidão.
    """
    hall_da_fama = []
    populacao = cria_populacao(TAMANHO_POPULACAO, pacientes)

    for _ in range(NUM_GERACOES):
        fitness = funcao_objetivo_pop(populacao)
        selecionados = selecao_torneio(populacao, fitness)
        
        proxima_geracao = []
        for pai, mae in zip(selecionados[::2], selecionados[1::2]):
            filho1, filho2 = cruzamento_ponto_simples(pai, mae, CHANCE_DE_CRUZAMENTO)
            proxima_geracao.append(filho1)
            proxima_geracao.append(filho2)
        
        for individuo in proxima_geracao:
            mutacao_troca(individuo, CHANCE_DE_MUTACAO)
        
        fitness = funcao_objetivo_pop(proxima_geracao)
        maior_fitness = max(fitness)
        indice = fitness.index(maior_fitness)
        hall_da_fama.append(proxima_geracao[indice])
        
        populacao = proxima_geracao
    
    fitness = funcao_objetivo_pop(hall_da_fama)
    maior_fitness = max(fitness)
    indice = fitness.index(maior_fitness)
    melhor_individuo_observado = hall_da_fama[indice]
    
    return melhor_individuo_observado, maior_fitness

```
## IMPORTANDO DADOS
Para utilização do algoritmo genético com seus próprios dados, é necessário importar os dados dos pacientes a partir de um arquivo CSV. Ou digitá-los manualmente, por meio de uma lista de dicionários, assim como é feito no notebook. O arquivo CSV deve seguir a seguinte estrutura:

# Estrutura do Arquivo CSV
O arquivo CSV deve conter as seguintes colunas:

**id**: Identificador único do paciente.
**idade**: Idade do paciente.
**genero**: Gênero do paciente (F para feminino, M para masculino).
**comorbidades**: Número de comorbidades do paciente.

# Bibliotecas

**Random**: _A biblioteca random do Python fornece ferramentas para gerar números pseudoaleatórios, permitindo a criação de sequências, seleções e embaralhamentos aleatórios._ [2]


# Referências

[1] RELATO DE EXPERIÊNCIA: O PROBLEMA DA FILA NUMA UNIDADE DE SAÚDE – RECIFE – PE; SARISECE, MARIA PACHÊCO VILELA. Disponível em: <https://www.cpqam.fiocruz.br/bibpdf/2010vilela-smp.pdf>. Acesso em: 28 abr. 2024.

[2]random — Generate pseudo-random numbers Disponível em: <https://docs.python.org/3/library/random.html>. Acesso em: 28 abr. 2024.
