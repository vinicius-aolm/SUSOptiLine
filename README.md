# SUSOptiLine
GRUPO 11, González, Gabriel; André, Vinicius.
ILUM ESCOLA DE CIENCIA, CAMPINAS 2024.
## Problematica

O Sistema Único de Saúde (SUS) é um dos maiores e mais complexos sistemas de saúde pública do mundo, responsável por fornecer atendimento médico a milhões de brasileiros. No entanto, um dos problemas mais persistentes e preocupantes que afetam o SUS é a longa espera e a demora no pronto atendimento[1]. As filas nos hospitais e postos de saúde se tornaram uma imagem comum, refletindo a sobrecarga dos serviços de saúde, a falta de recursos e a gestão ineficiente. Este cenário resulta em atrasos críticos no diagnóstico e tratamento, impactando negativamente a saúde e a qualidade de vida dos pacientes. 
Pensando nisso, em nosso trabalho final de algoritmos genéticos, decidimos desenvolver um algoritmo genético para otimizar filas de espera no Sistema Único de Saúde (SUS) do Brasil, considerando fatores como idade, gênero e comorbidades para priorização de atendimento.
Contribuições e feedbacks são bem-vindos.

## SUSOptiLine
![MioCard (3)](https://github.com/vinicius-aolm/SUSOptiLine/assets/135054073/7b660a6b-496f-4935-9502-bba2137cf785)
Contribuições e feedbacks são bem-vindos.

# Organização do GIT.
Redme: Resumo e visão geral do projeto.

Notebooks: 

-SUSOptiline-Building.ipynb

-SUSOptiline.ipynb


# Banco de dados:
-Pacientes.csv

O Banco de dados apresenta 150 pacientes hipoteticos, criados pela propia equipe.
Organizados por id, idade, genero e comorbidades.

tais dados tambem estão disponiveis no notebook SUSOptiLine.ipynb em forma de lista de dicionário.
# Glossario de Funções

Disponiveis em funçoes.py.

**criar_gene**: Gera um gene (indivíduo) representando um paciente.

**cria_populacao**: Cria a população inicial de indivíduos.

**calcular_aptidao**: Calcula a aptidão de um indivíduo com base nos critérios definidos (idade e comorbidades).

**funcao_objetivo_pop**: Calcula a aptidão de toda a população.

**selecao_torneio**: Seleciona indivíduos para reprodução com base em um torneio.

**cruzamento_ponto_simples**: Realiza o cruzamento de dois indivíduos para gerar novos indivíduos.

**mutacao_troca**: Aplica mutações aos indivíduos para introduzir variação genética.

# Construção do Algoritimo
### 1. Parâmetros do Algoritmo Genético

Os principais parâmetros do algoritmo genético são:

**Tamanho da População**: Número de possíveis soluções (indivíduos) em cada geração.

**Número de Gerações**: Quantidade de iterações que o algoritmo vai executar.

**Chance de Cruzamento**: Probabilidade de que dois indivíduos se cruzem para formar novos indivíduos.

**Chance de Mutação**: Probabilidade de que um indivíduo sofra uma mutação.

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

```
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
```
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
```
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

```
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
```
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
```
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
 **Seleção por Torneio**: Indivíduos competem em pequenos torneios e o melhor de cada torneio é selecionado. É simples e eficaz, especialmente quando há grande variabilidade na aptidão.
 
**Seleção por Roleta**: Indivíduos são selecionados com probabilidade proporcional à sua aptidão. É menos eficiente quando há pouca diferença na aptidão dos indivíduos.

#### Optamos por usar seleção por torneio porque é mais robusta em cenários onde há grande variabilidade na aptidão, garantindo que os melhores indivíduos sejam frequentemente selecionados.

### 8.Cruzamento de Ponto Simples

O cruzamento combina partes de dois genes para criar novos genes. Vamos implementar uma função para cruzamento de ponto simples:
```
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
```
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


# Bibliotecas

**Random**: _A biblioteca random do Python fornece ferramentas para gerar números pseudoaleatórios, permitindo a criação de sequências, seleções e embaralhamentos aleatórios._


# Referências

[1] RELATO DE EXPERIÊNCIA: O PROBLEMA DA FILA NUMA UNIDADE DE SAÚDE – RECIFE – PE; SARISECE, MARIA PACHÊCO VILELA. Disponível em: <https://www.cpqam.fiocruz.br/bibpdf/2010vilela-smp.pdf>. Acesso em: 28 abr. 2024.


