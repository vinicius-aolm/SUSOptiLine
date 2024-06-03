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

# Bibliotecas

**Random**: _A biblioteca random do Python fornece ferramentas para gerar números pseudoaleatórios, permitindo a criação de sequências, seleções e embaralhamentos aleatórios._


# Referências

[1] RELATO DE EXPERIÊNCIA: O PROBLEMA DA FILA NUMA UNIDADE DE SAÚDE – RECIFE – PE; SARISECE, MARIA PACHÊCO VILELA. Disponível em: <https://www.cpqam.fiocruz.br/bibpdf/2010vilela-smp.pdf>. Acesso em: 28 abr. 2024.


