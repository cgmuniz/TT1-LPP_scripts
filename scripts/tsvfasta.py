with open('/home/administrator/Documentos/Teste_fa_igblast_db-pass_parse-select.tsv', 'r') as tsv_file:
    with open('/home/administrator/Documentos/Teste_fa_analise.fasta', 'w') as fasta_file:
        for line in tsv_file:
            columns = line.strip().split('\t')
            cdr1 = columns[45]  # Replace with the appropriate column index
            cdr2 = columns[46]  # Replace with the appropriate column index
            cdr3 = columns[47]  # Replace with the appropriate column index
            
            full_sequence = cdr1 + cdr2 + cdr3
            fasta_file.write(f'>{columns[0]}\n{full_sequence}\n')

