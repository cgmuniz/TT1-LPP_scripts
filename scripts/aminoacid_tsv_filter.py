import pandas as pd
import sys

argvs = sys.argv
path = argvs[1]
output = argvs[2]

tabela = pd.read_csv(path, sep='\t')

counter = tabela.groupby(['junction_aa','v_call']).size().reset_index(name='contagem')
counter_result = counter[['junction_aa','v_call', 'contagem']]

counter_result.to_csv(output, sep='\t', index=False)
