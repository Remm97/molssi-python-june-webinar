import os
import argparse

#Tell argparse to handle arguments
parser = argparse.ArgumentParser(description="This script parses amber mdout files to extract the total energy.")

#Tell argparse what arguments to expect
parser.add_argument("path", help="The filepath to the file to be analyzed.")

#Get arguments from the user
args = parser.parse_args()

# Open file for reading
filename = args.path
f = open(filename, 'r')

# Read data in file
data = f.readlines()
f.close()

# Open a file for writing
base_filename = filename.split('.')[0]
f_write = open(F'{base_filename}_EtotAK.txt', 'w+')

print(F'Writing output to {base_filename}')

f_write.write('Total Energy\n')

etot = []
# Get info from line
for line in data:
    split_line = line.split()
    
    if 'Etot' in line:
        #print(split_line[2])
        etot.append(split_line[2])
        
#slicing to include everything but the last 2
etot = etot[:-2]

for energy in etot:
    f_write.write(F"{energy}\n")

# Write info to new file
f_write.close()