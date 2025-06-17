import pandas as pd
import os
from langchain.chat_models import ChatOpenAI
from langchain.agents import create_pandas_dataframe_agent
from dotenv import load_dotenv

# Carregar chave API
load_dotenv()

# Caminhos
extract_path = 'extracted_files/'
cabecalho_path = os.path.join(extract_path, '202401_NFs_Cabecalho.csv')
itens_path = os.path.join(extract_path, '202401_NFs_Itens.csv')

# Carregar CSVs
df_cabecalho = pd.read_csv(cabecalho_path)
df_itens = pd.read_csv(itens_path)

# Criar modelo
llm = ChatOpenAI(model_name='gpt-4o', temperature=0)

# Criar agente
agent = create_pandas_dataframe_agent(
    llm,
    [df_cabecalho, df_itens],
    verbose=True
)

def responder_pergunta(pergunta):
    resposta = agent.run(pergunta)
    return resposta
