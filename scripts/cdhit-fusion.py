import re
import pandas as pd

tabela = pd.read_csv('MinION.tsv', sep='\t')
#tabela = pd.read_excel('MinION.xlsx')

# Função para extrair informações de um arquivo .clstr
def extract_clstr_info(clstr_file):
    clusters = []
    with open(clstr_file, 'r') as f:
        lines = f.readlines()
        current_cluster = None
        for line in lines:
            if line.startswith(">Cluster"):
                if current_cluster:
                    clusters.append(current_cluster)
                current_cluster = {'name': line.strip()}
            else:
                match = re.search(r'>(.+?)\.\.\.\s+at\s+([\d.]+)%', line)
                if match:
                        current_cluster['sequences'].append({'name': match.group(1), 'similarity': float(match.group(2))})
                else:
                    match = re.search(r'>(.+?)\.\.\.', line)
                    if match:
                      current_cluster['covabdab_sequence'] = match.group(1)
                      current_cluster['sequences'] = []
        if current_cluster:
            clusters.append(current_cluster)
    return clusters

# Função para adicionar informações à tabela
def update_table(table, clusters):
    for cluster in clusters:
        covabdab_sequence = cluster['covabdab_sequence']
        for sequence in cluster['sequences']:
            sequence_name = sequence['name']
            similarity = sequence['similarity']
            # Procura a linha correspondente na tabela e adiciona as informações
            for index, row in table.iterrows():
                if sequence_name == row['junction_aa']:
                    table.at[index, 'covabdab_sequence'] = covabdab_sequence
                    table.at[index, 'similarity_percentage'] = similarity

# Exemplo de uso
clstr_file = '/home/administrator/Documentos/MinION/cdhit/iglv_80.clstr'
# Supondo que você já tenha sua tabela carregada em um DataFrame chamado 'tabela'
clusters = extract_clstr_info(clstr_file)
update_table(tabela, clusters)

tabela.to_csv('MinION.tsv', sep='\t', index=False)
