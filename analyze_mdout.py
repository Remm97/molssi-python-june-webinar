import os
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This script analyzes a user provided mdout file and outputs Etot.")
    parser.add_argument("mdout_file", help="The filepath for the mdout file to analyze")
    parser.add_argument('Path', metavar='path', type=str, help='the path to mdout files')
    args = parser.parse_args()
    mdout_file = args.path

#below function creates path to files, * = wild card
file_location = os.path.join('data', '03_Prod.mdout')
print(file_location)

filename = os.path.basename(args.path).split('.')[0]
print(filename)

filehandle = open('filename_etot.txt','w+')
filehandle.write(F' NSTEP \t Time (ps) \t Etot (kcal/mol) \t Temp (K) \t Press \n')

#open for reading (below)
outfile = open(file_location, 'r')
#below we are pulling in all data using readlines
data = outfile.readlines()
#then closing file
outfile.close()


for line in data:
    if 'Etot' in line:
        energy_line = line
        #split line into its words
        etot_words = energy_line.split()
        etot = etot_words[2]
#        print(etot_label, etot)       

    if 'NSTEP' in line:
        iteration_line = line
        #split line into its words
        iteration_words = iteration_line.split()
        iteration = iteration_words[2]
#        print(iteration_label, iteration)
    
    if 'TIME(PS)' in line:
        time_line = line
        #split line into its words
        time_words = time_line.split()
        time = time_words[5]
#        print(time_label, time)
        
    if 'TEMP(K)' in line:
        temp_line = line
        #split line into its words
        temp_words = temp_line.split()
        temp_label = temp_words[6]
        temp = temp_words[8]
#        print(temp_label, temp_words)
    
    if 'PRESS' in line:
        press_line = line
        #split line into its words
        press_words = press_line.split()
#        press_label = press_words[9]
        press = press_words[11]
#        print(ppress_words)

        filehandle.write(F' {iteration} \t {time} \t {etot} \t {temp} \t {press} \n')


    if 'A V E R A G E S' in line:
        break
        

filehandle.close()