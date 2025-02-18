#pyprocesser
import sys



coords_file = sys.argv[1] + ".coords"

ids = []
ids.append(sys.argv[1])

with open(coords_file, 'r') as file:
	data = file.readlines()[5:]
	for line in data:
		val = (line.strip()[-1])
		ids.append(val)
#open the .coords file
#look for line 5
#pull last character join with \t
MLST = '\t'.join(ids)



with open('MLST_results.txt','a') as out_file:
    out_file.write(MLST + "\n")
