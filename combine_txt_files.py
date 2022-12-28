import os, glob
files = glob.glob('res\*.txt')

all_lines = []
for f in files:
    try:
        with open(f,'r') as fi:
            all_lines += fi.readlines()
    except UnicodeDecodeError:
        print('Skipping this word, weird character')
        continue
all_lines = set(all_lines)

with open('res/combinedfile.txt','w') as fo:
    fo.write("".join(all_lines))