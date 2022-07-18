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

for x in range(5000):#tentativas
    r_letras = []
    area_total = 0
    #criando uma frase randomicamente
    for i in range(n_matriz):
        a = r.choice(["A","B","C","D"])
        r_letras.append(a)
        
    #calculo da area realtivo a frase randon 
    for j in r_letras:
        index = ["A","B","C","D"].index(j)        
        area_total = area_total + opa[index]
        
    #select facade
    media = area_total/n_matriz    
    if media<30:
        sul.append(r_letras)
        s=s+1
    elif media> 60:
        norte.append(r_letras)
        n=n+1
        
def index_wrap(option, list):
    number  = len(list)
    if option > number:
        number = number - option
    else:
       number  = option
    return number
print(index_wrap(9,[x for x in range(50)]))
#norte = gh.TreeBranch(gh.SimplifyTree(gt.list_to_tree(norte),True), option_norte) 
#sul = gh.TreeBranch(gh.SimplifyTree(gt.list_to_tree(sul),True), option_sul) 
print("sul: ",s)
print("norte: ",n)
#norte = norte[]