import os 
import re
from collections import defaultdict
tcount=set()
gcount=set()
path='/home/deepanshi/projects/mxe4/gex7'
files = os.listdir(path)
names=[]
d={}
kc=0
for f in files:
    ff='/home/deepanshi/projects/mxe4/gex7/'+f
    with open (ff,'r') as f1: 
        d={}
        kc=0
        for line in f1:
            line=line.strip('\n')
            a=re.search("^\w",line)
            if a:
                kc=9
                el=re.split('\t',line)
                tid=el[0]
                ex=el[3] 
                dex=el[2]
            
                if dex=='0':
                    num=el[4]
                    print(num)
                    if num=='2':
                        print(tid,ex)
                        
                        d.update({tid:ex})
        if kc==9:                
            with open('/home/deepanshi/projects/mxe4/gex8/'+f,'w') as f2:
                for j in d:
                    f2.write('{}\t{}\n'.format(j,d[j]))  
                    tcount.add(j)
                    gcount.add(f)           

with open('cg_9','w') as f3:
    for k in gcount:
        f3.write("{}\n".format(k))

with open('ct_9','w') as f3:
    for ik in tcount:
        f3.write("{}\n".format(ik))        