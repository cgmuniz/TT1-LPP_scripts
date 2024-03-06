import csv
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

# Caminho para o arquivo TSV com as informações do IgBLAST
input_csv_file = "/home/administrator/Downloads/junction_aa_MinION-2024.csv"

# Caminho para o arquivo de saída FASTA com as sequências de aminoácidos CDR3 traduzidas
output_fasta_file = "/home/administrator/Downloads/junction_aa_MinION-2024.fasta"

# Lista para armazenar os registros FASTA
cdr_sequences = []

# Abrir o arquivo TSV e processar as informações
with open(input_csv_file, "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        # Extrair as sequências CDR1, CDR2 e CDR3 do TSV
        #cdr1_sequence = row["cdr1"]
        #cdr2_sequence = row["cdr2"]
        cdr3_sequence = row["junction_aa"]

        # Criar registros FASTA para cada sequência CDR
        #cdr_record = SeqRecord(Seq(cdr1_sequence+cdr2_sequence+cdr3_sequence), id=row["sequence_id"], description="")
        cdr_record = SeqRecord(Seq(cdr3_sequence), id=row["junction_aa"], description="")
        
        # Adicionar registros à lista
        cdr_sequences.extend([cdr_record])

# Salvar as sequências CDR1, CDR2 e CDR3 em um arquivo FASTA
SeqIO.write(cdr_sequences, output_fasta_file, "fasta")
