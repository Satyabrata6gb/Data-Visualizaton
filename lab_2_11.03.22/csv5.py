import sys
import csv

n=len(sys.argv)
number=0
if n!=2:
    print("Enter proper arguments")
else:
    filename=sys.argv[1]
    f=open(filename,'r')
    rows=[]
    csvreader=csv.reader(f)
  
    m={}
    i=1
    for row in csvreader:
        if(row[0]=='Sno'):
            for col in row:
                m[col]=i
                i=i+1
            break
    print(m)
