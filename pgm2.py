import re
from collections import defaultdict
import os
d={}
with open('/home/deepanshi/projects/8-mer comb/pa_map.txt','r') as f:
    for line in f:
        line=line.strip('\n')
        el=re.split('[\t]',line)
        pep=el[0]
        g=re.split('[\s]',el[1])
        gid=g[0]
        #print(pep,gid)
        d.update({pep:gid})
with open('pep_genemap.txt','w') as f1:
    gs=defaultdict(set)
   
    path='/home/deepanshi/projects/8-mer comb/genjunc'
    files = os.listdir(path)
    names=[]
    for fn in files:
        count=0
        ff=path+'/'+fn
        with open(ff,'r') as f2:
            for line in f2:
                line=line.strip('\n')
                pep=line 
                gs[pep].add(fn[0:-3]) 
                 
gsd=dict(gs)
for i in d:
    for j in gsd:
        if j in i:
           
            f1.write("{}\t{}\t{}\n".format('Peptide','PA_gene','Predicted gene'))
            f1.write("{}\t{}\t{}\n".format(i,d[i],gsd[j]))                    
                                
                