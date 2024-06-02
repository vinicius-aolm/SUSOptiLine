import random

def criar_gene(pacientes):
    """
    Cria um gene (uma ordem de pacientes).

    Args:
        pacientes (list): Lista de dicionários representando os pacientes.

    Returns:
        list: Lista embaralhada de pacientes.
    """
    gene = pacientes[:]  # Copia superficial para preservar a lista original
    random.shuffle(gene)  # Embaralha a ordem dos pacientes
    return gene

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

def funcao_objetivo_pop(populacao):
    """
    Calcula a aptidão para toda a população.

    Args:
        populacao (list): Lista de genes (população).

    Returns:
        list: Lista de valores de aptidão para cada gene.
    """
    return [calcular_aptidao(gene) for gene in populacao]

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
