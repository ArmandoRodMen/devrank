#Alinear Objetos v0.1
#Armando Rodriguez 
#Alinear Objetos en un espacio tridimensional


import maya.cmds as cmds #importar biblioteca de maya a python

sel = cmds.ls(selection=True) #crear lista de objetos seleccionados
lsel = len(sel) #largo del index selección
print sel #se imprime lista de seleccionados 

a=0 #variable neutra a incrementar más adelante para un segundo index
for i in range(lsel-1):#declaración de bucle "for" hasta el largo de la selección menos una unidad 

#Obtener radio, traslación y rotación de "i"
    a=a+1 #incremento de la variable neutra

    tra = cmds.xform (sel[i], query=True, worldSpace=True, translation=True) #"xform" para obteción de traslación de manera en cola
    rot = cmds.xform (sel[i], query=True, worldSpace=True, rotation=True) #"xform" para obteción de rotaciónn de manera en cola
    print a, i
    
#Mover a selección maestra

    cmds.xform (sel[a], worldSpace=True, translation=tra) #"xform" para mover selección con index A a lo obtenido en selección index i
    cmds.xform (sel[a], worldSpace=True, rotation=rot) #"xform" para rotar selección con index A a lo obtenido en selección index i
    cmds.select(clear=True) #limpiar selección

#Fin de script