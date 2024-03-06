import re
import sys
from Bio import SeqIO

  # Deve-se instalar biopython antes: pip install biopython

argvs = sys.argv
path = argvs[1]
nSeq = int(argvs[2])

if len(sys.argv) < 4:
    print("Uso: python3 buscaSeq.py <caminho_fasta> <num_fragmentos> <frag1> <frag2> ...")
    sys.exit(1)
    
  # Arquivos fasta
  
for i in range(nSeq):
  seq = argvs[i + 3]

  with open(path) as fasta_file:
      for record in SeqIO.parse(fasta_file, "fasta"):
          sequence = str(record.seq)
          pattern = re.compile(rf'(\S{{0,6}}){re.escape(seq)}(\S{{0,6}})')
          match = pattern.search(sequence)
          if match is not None:
              left_context = match.group(1)
              right_context = match.group(2)
              print(f"Cabeçalho: {record.id}")
              print(f"Sequência: {sequence}")
              print(f"6 caracteres à esquerda: {left_context}")
              print(f"6 caracteres à direita: {right_context}")
              break
      else:
          print(f"Sequência {seq} não encontrada")
