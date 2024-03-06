import pandas as pd
import sys

argvs = sys.argv
path = argvs[1]
output = argvs[2]

tabela = pd.read_csv(path, sep='\t')

expanded_data = [(j_aa, v_call) for j_aa, v_calls in tabela[['junction_aa', 'v_call']].values for v_call in v_calls.split(',')]

expanded_df = pd.DataFrame(expanded_data, columns=['junction_aa', 'v_call'])

counter = expanded_df.groupby(['junction_aa', 'v_call']).size().reset_index(name='contagem')

counter.to_csv(output, sep='\t', index=False)
