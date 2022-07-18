import rhinoscriptsyntax as rs
import ghpythonlib.components as gh
import Rhino.Geometry as rg

def porcentagem(surface):    
    area,_ = gh.Area(surface)     
    area_t,_  =  gh.MassAddition(area)    
    num = round(((area_t/9)*100),2)
    return num


opa_A, opa_B = porcentagem(A),porcentagem(B)
opa_C, opa_D = porcentagem(C),porcentagem(D)
opa = [opa_A, opa_B, opa_C, opa_D]