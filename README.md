# Introdução
![MioCard (3)](https://github.com/vinicius-aolm/SUSOptiLine/assets/135054073/7b660a6b-496f-4935-9502-bba2137cf785)

## SUSOptiLine

Desenvolvimento de um algoritmo genético para otimizar filas de espera no Sistema Único de Saúde (SUS) do Brasil, considerando fatores como idade, gênero e comorbidades para priorização de atendimento. 
Contribuições e feedbacks são bem-vindos.

<details>
  <summary>Organização do GIT</summary>

  - Redme: Resumo e visão geral do projeto.
  
  - Notebooks: 
    - SUSOptiline-Building.ipynb
    - SUSOptiline.ipynb

</details>

<details>
  <summary>Banco de dados</summary>

  - Pacientes.csv
  
  O Banco de dados apresenta 150 pacientes hipotéticos, criados pela própria equipe. Organizados por id, idade, gênero e comorbidades.
  Tais dados também estão disponíveis no notebook SUSOptiLine.ipynb em forma de lista de dicionário.

</details>

<details>
  <summary>Funções</summary>

  - Disponíveis em funções.py
  
  - criar_gene: Gera um gene (indivíduo) representando um paciente.
  
  - criar_populacao: Cria a população inicial de indivíduos.
  
  - calcular_aptidao: Calcula a aptidão de um indivíduo com base nos critérios definidos (idade e comorbidades).
  
  - funcao_objetivo_pop: Calcula a aptidão de toda a população.
  
  - selecao_torneio: Seleciona indivíduos para reprodução com base em um torneio.
  
  - cruzamento_ponto_simples: Realiza o cruzamento de dois indivíduos para gerar novos indivíduos.
  
  - mutacao_troca: Aplica mutações aos indivíduos para introduzir variação genética.

</details>

<details>
  <summary>Bibliotecas</summary>

  - Adicione a lista de bibliotecas aqui.

</details>
