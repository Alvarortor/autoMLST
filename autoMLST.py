#Automates any process onto several isolates
import os
import sys
import re
import time

#Gene file
my_file = sys.argv[1]

#How long
t_start = time.time() 



#Make list to store commands
NUC_commands = list()


#Find the file
path = os.path.abspath(my_file)
file = open(path, 'r')

#Create output
out_file = open('MLST_results.txt', 'w')




for line in file:
	line = line.strip()
    	nuc = "./nucmer -maxmatch -c 100 " + line + ".fasta MLST.fasta"
    	process_data = "./show-coords  -I 100 out.delta > " + line + ".coords"
    	get_MLST = "python pyprocesser.py " + line
   	 #need a python script for here to process the actual data

	NUC_commands.append(nuc)
	NUC_commands.append(process_data)
	NUC_commands.append(get_MLST)
    	

    

count = 0
for line in NUC_commands:
	try:
    		os.system(line)
    		print(line)
    		count += 1
	except Exception as e:
		print(e)
		print("Error - Pausing program. Press enter to resume")
		input()

    

t_stop = time.time() 
time_diff = (t_stop - t_start)
time_diff = round(time_diff,3)
done_mess = ("All Done! Ran " + str(count) + " commands in " + str(time_diff) + "(s)")
print(done_mess)