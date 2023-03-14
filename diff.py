C=[]
CC=[]
N=[]
NN=[]


new_f=input("write the path of the first file: ")
current_f=input("write the path of the second file: ")
filee=input("write the path of the output file: ")


with open(current_f,'r') as current:
    for line in current:
        C.append(line.replace("\n", " "))

with open(new_f, 'r') as new:
    for line in new:
        N.append(line.replace("\n", " "))

        
with open(filee,'w') as dif:
    for x in C:
        if x not in N:
            dif.write(x+"\n")

