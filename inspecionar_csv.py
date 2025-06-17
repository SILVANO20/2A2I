import pandas as pd
import os

extract_path = 'extracted_files/'

cabecalho_path = os.path.join(extract_path, '202401_NFs_Cabecalho.csv')
itens_path = os.path.join(extract_path, '202401_NFs_Itens.csv')

# Carregar CSVs
df_cabecalho = pd.read_csv(cabecalho_path)
df_itens = pd.read_csv(itens_path)

# Inspecionar colunas
print("Colunas do Cabeçalho:")
print(df_cabecalho.columns)

print("\nColunas dos Itens:")
print(df_itens.columns)
