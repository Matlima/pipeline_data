from processamento_dados import Dados


path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'

# Extract

print('Extração de dados')

print('Empresa A')
dados_empresaA = Dados(path_json, 'json')
print('Colunas dos dados:')
print(dados_empresaA.nome_colunas)
print('Quantidade de linhas:')
print(dados_empresaA.qtd_linhas)

print('---------------------------------')

print('Empresa B')
dados_empresaB = Dados(path_csv, 'csv')
print('Colunas dos dados:')
print(dados_empresaB.nome_colunas)
print('Quantidade de linhas:')
print(dados_empresaB.qtd_linhas)

# Transform
print('---------------------------------')

print('Transformação de dados')
print('Colunas de dados atualizadas:')
key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}

dados_empresaB.rename_columns(key_mapping)
print('Colunas dos dados:')
print(dados_empresaB.nome_colunas)

print('Fusão de dados')
dados_fusao = Dados.join(dados_empresaA, dados_empresaB)
print(dados_fusao)
print('Colunas dos dados:')
print(dados_fusao.nome_colunas)
print('Quantidade de linhas:')
print(dados_fusao.qtd_linhas)

# Load

path_dados_combinados = 'data_processed/dados_combinados.csv'
dados_fusao.salvando_dados(path_dados_combinados)
print(path_dados_combinados)

