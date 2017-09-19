import pandas as pd
import os
csv_file=pd.read_csv("corpus.csv",encoding="ISO-8859-1")
os.chdir("ir_project")
for i in range(1,600):
	k=i
	filename=str(k)+".txt"
	f=open(filename,"w+")
	f.write(csv_file.loc[i]["body"])
	f.close()

