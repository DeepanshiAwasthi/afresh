import os 
import re
from collections import defaultdict
path='/home/deepanshi/projects/mxe4/gex'
files = os.listdir(path)
names=[]
d={}
for f in files:
    ff='/home/deepanshi/projects/mxe4/gex/'+f
    with open (ff,'r') as f1: 
        for line in f1: