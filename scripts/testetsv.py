import pandas as pd
import sys

argvs = sys.argv
path = argvs[1]
output = argvs[2]

tabel = pd.read_csv(path, sep='\t')


