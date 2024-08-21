# Data Pipeline Project

## Descrição
Este projeto foi desenvolvido para criar um pipeline de dados eficiente e reutilizável, que integra duas fontes de dados distintas e fornece esses dados unidos para o time de Product Insights (PI). O projeto foi inicialmente conduzido através da exploração de dados no Jupyter Notebook, utilizando conceitos fundamentais de Python e bibliotecas como JSON e CSV. Posteriormente, o código foi refatorado para um script independente, implementando programação orientada a objetos para facilitar o processo e garantir a reutilização do pipeline.

## Objetivos do Projeto
- Unificação de Fontes de Dados: Criar um pipeline que combine dados de duas fontes diferentes e forneça esses dados unidos de forma coesa.
- Reutilização: Desenvolver um pipeline que possa ser facilmente adaptado para futuros projetos com requisitos semelhantes.
- Eficiência: Refatorar o código para otimizar o pipeline, utilizando técnicas de programação orientada a objetos.

## Tecnologias Utilizadas
- Python: Linguagem principal utilizada para desenvolvimento do pipeline.
- Jupyter Notebook: Ambiente inicial para exploração de dados e prototipagem.
- Bibliotecas Python:
  - JSON: Para manipulação e leitura de dados no formato JSON.
  - CSV: Para manipulação e leitura de arquivos CSV.
- Programação Orientada a Objetos: Refatoração do pipeline em um script Python, utilizando classes e funções para modularidade e reutilização.

## Estrutura do Projeto
- data_pipeline.ipynb: Notebook Jupyter onde a exploração de dados inicial foi realizada, incluindo testes e validação do pipeline.
- data_pipeline.py: Script Python refatorado que contém a implementação final do pipeline, utilizando programação orientada a objetos.
 - Pipeline Class: Classe principal que encapsula a lógica do pipeline de dados, tornando o processo mais organizado e reutilizável.
 - Funções Auxiliares: Conjunto de funções para manipulação de dados, leitura e escrita em JSON e CSV.

## Como Executar
- Exploração Inicial:
  - Abra o arquivo data_pipeline.ipynb no Jupyter Notebook.
  - Execute as células para explorar os dados e entender o fluxo do pipeline.

- Execução do Pipeline:
  - Execute o script data_pipeline.py no terminal ou em qualquer ambiente Python.
  - Certifique-se de ter os arquivos de dados em JSON e CSV na pasta correta.
  - O pipeline unirá os dados das duas fontes e gerará um arquivo de saída contendo os dados combinados.

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests.

## Licença
Este projeto está licenciado sob a MIT License.

## Desenvolvidor por:
Matheus de Lima Rios
