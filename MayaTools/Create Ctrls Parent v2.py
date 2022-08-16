#Armando Rodriguez
#Create Ctrls Parent v2
#Crea un control emparentado en grupo donde está seleccionado el joint

import maya.cmds as cmds #Importar biblioteca de comandos
sel = cmds.ls(selection=True) #Crear lista de objetos seleccionados

for i in sel: #Bucle "for" hasta terminar selección

    rad = cmds.getAttr (i + ".radius") #Obtener el radio del Joint
    tra = cmds.xform (i, query=True, worldSpace=True, translation=True) #"xform" para obteción de traslación de manera en cola
    
    ctr = cmds.circle (normal=(0,1,0), radius=rad*1.25, name="Ctrl_"+i) #Crear control curva
    grp = cmds.group (name="Grp_"+i) #Crear grupo control emparentando control curva
    
    cmds.select(clear=True) #Limpiar selección 
    cmds.xform (grp, worldSpace=True, translation=tra) #mover grpo creado a traslación del Joint
    cmds.xform (grp, worldSpace=True)
    
    cmds.parentConstraint(ctr[0], i) 
    cmds.scaleConstraint(ctr[0], i)
    
#Fin de Script