
import rhinoscriptsyntax as rs
import ghpythonlib.components as gh
import ghpythonlib.treehelpers as gt

def order_phrase (seed,letters):
    random_phrase = list(gh.Jitter(letters,1,seed))
    #print(type(random))
    #random_phrase = letters
    return random_phrase[0]
phrase = order_phrase(seed,letters)


print(phrase)
def geometry(A,B,C,D,phrase,vec):
    list_breps = []
    for i in phrase: 
        #print(i)
        if i =="A":
            item = A
        elif i =="B":
            item = B
        elif i =="C":
            item = C
        else:
            item = D
            
        list_breps.append(item)
       
    geo,_ = gh.Move(list_breps,vec)
    
    return geo
fm = geometry(A,B,C,D,phrase,vec)