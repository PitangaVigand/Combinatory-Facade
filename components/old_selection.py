
import rhinoscriptsyntax as rs
import ghpythonlib.components as gh
import ghpythonlib.treehelpers as gt
import Rhino.Geometry as rg
import random as r

n_matriz = n*m
r_letras = []
area_total = 0
norte = []
sul = []
s = 0
n = 0
opa_sul = 30
opa_norte = 60
letras = ["A","B","C","D"]


for x in range(5000):#tentativas
    r_letras = []
    area_total = 0
    #criando uma frase randomicamente
    for i in range(n_matriz):
        a = r.choice(letras)
        r_letras.append(a)
        
    #calculo da area realtivo a frase randon 
    for j in r_letras:
        index = letras.index(j)        
        area_total = area_total + opa[index]
        
    #select facade
    media = area_total/n_matriz    
    if media<opa_sul:
        sul.append(r_letras)
        s=s+1
    elif media> opa_norte:
        norte.append(r_letras)
        n=n+1
        


#norte = gh.TreeBranch(gh.SimplifyTree(gt.list_to_tree(norte),True), option_norte) 
#sul = gh.TreeBranch(gh.SimplifyTree(gt.list_to_tree(sul),True), option_sul) 
print("sul: ",s)
print("norte: ",n)
norte = norte[option_norte if option_norte<n else option_norte-n]