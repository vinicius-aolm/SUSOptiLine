# Introdução
## SUSOptiLine
Desenvolvimento de um algoritmo genético para otimizar filas de espera no Sistema Único de Saúde (SUS) do Brasil, considerando fatores como idade, gênero e comorbidades para priorização de atendimento. 
Contribuições e feedbacks são bem-vindos.

# Organização do GIT.
Redme: Resumo e visão geral do projeto.
Notebooks: 
-notebook tal ai(.ipynb)

#Banco de dados:
-Pacientes.csv
O Banco de dados apresenta 150 pacientes hipoteticos, criados pela propia equipe.
Organizados por id,idade, genero e comorbidades.
tais dados tambem estão disponiveis no notebook SUSOptiLine.ipynb em forma de lista de dicionário.
# Funçoes
criar_gene: Gera um gene (indivíduo) representando um paciente.
cria_populacao: Cria a população inicial de indivíduos.
calcular_aptidao: Calcula a aptidão de um indivíduo com base nos critérios definidos (idade e comorbidades).
funcao_objetivo_pop: Calcula a aptidão de toda a população.
selecao_torneio: Seleciona indivíduos para reprodução com base em um torneio.
cruzamento_ponto_simples: Realiza o cruzamento de dois indivíduos para gerar novos indivíduos.
mutacao_troca: Aplica mutações aos indivíduos para introduzir variação genética.

# Bibliotecas
