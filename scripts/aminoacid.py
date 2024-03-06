import csv
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

# Caminho para o arquivo TSV com as informações do IgBLAST
input_tsv_file = "/data8/AKT/20221129_pcr2coronavac/no_sample/20221129_2102_MC-110697_FAU75433_22d65ffd/fastq/barcode01/chopper/fasta/analise/filtered_20221129_barcode01_igblast_db-pass_parse-select.tsv"

# Caminho para o arquivo de saída FASTA com as sequências de aminoácidos CDR3 traduzidas
output_fasta_file = "/data8/AKT/20221129_pcr2coronavac/no_sample/20221129_2102_MC-110697_FAU75433_22d65ffd/fastq/barcode01/chopper/fasta/analise/cdr_sequences.fasta"

# Lista para armazenar os registros FASTA
cdr_sequences = []

# Caminho para o arquivo FASTA com as sequências CDR1, CDR2 e CDR3
input_fasta_file = "/data8/AKT/20221129_pcr2coronavac/no_sample/20221129_2102_MC-110697_FAU75433_22d65ffd/fastq/barcode01/chopper/fasta/analise/cdr_sequences.fasta"

# Caminho para o arquivo de saída FASTA com as sequências de aminoácidos traduzidas
output_amino_acid_file = "/data8/AKT/20221129_pcr2coronavac/no_sample/20221129_2102_MC-110697_FAU75433_22d65ffd/fastq/barcode01/chopper/fasta/analise/cdr_amino_acid.fasta"

# Lista para armazenar os registros FASTA traduzidos em aminoácidos
translated_sequences = []

# Abrir o arquivo TSV e processar as informações
with open(input_tsv_file, "r") as tsv_file:
    tsv_reader = csv.DictReader(tsv_file, delimiter="\t")
    for row in tsv_reader:
        # Extrair as sequências CDR1, CDR2 e CDR3 do TSV
        #cdr1_sequence = row["cdr1"]
        #cdr2_sequence = row["cdr2"]
        cdr3_sequence = row["cdr3"]

        # Criar registros FASTA para cada sequência CDR
        #cdr_record = SeqRecord(Seq(cdr1_sequence+cdr2_sequence+cdr3_sequence), id=row["sequence_id"], description="")
        cdr_record = SeqRecord(Seq(cdr3_sequence), id=row["sequence_id"], description="")
        
        # Adicionar registros à lista
        cdr_sequences.extend([cdr_record])

# Salvar as sequências CDR1, CDR2 e CDR3 em um arquivo FASTA
SeqIO.write(cdr_sequences, output_fasta_file, "fasta")

# Abrir o arquivo FASTA e processar as sequências
with open(input_fasta_file, "r") as fasta_file:
    for record in SeqIO.parse(fasta_file, "fasta"):
        # Traduzir a sequência de nucleotídeos em aminoácidos
        amino_acid_sequence = str(record.seq.translate())
        
        # Criar um novo registro FASTA com a sequência de aminoácidos traduzida
        translated_record = SeqRecord(Seq(amino_acid_sequence), id=record.id, description="")
        translated_sequences.append(translated_record)

# Salvar as sequências traduzidas em um arquivo FASTA
SeqIO.write(translated_sequences, output_amino_acid_file, "fasta")
