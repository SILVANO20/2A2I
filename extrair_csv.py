import zipfile
import os

# Caminhos
zip_path = '202401_NFs.zip'
extract_path = 'extracted_files/'

# Certifique-se de que a pasta existe
os.makedirs(extract_path, exist_ok=True)

# Extrair o arquivo
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

print(f"Arquivos extraídos para: {extract_path}")
