#Armando
#rivetCreator.py
#Seleccionar el Rivet para crear Joint emparentado


import maya.cmds as cmds #importar biblioteca de comandos
sel = cmds.ls(selection=True) #crear lista de objetos seleccionados
lsel = len(sel) #largo del index selección

for i in range (lsel): #ciclo "for", denrto de la lista "sel"

    tra = cmds.xform (sel[i], query = True, worldSpace = True, translation = True) #"xform" para obteción de traslación de manera en cola
    rot = cmds.xform (sel[i], query = True, worldSpace = True, rotation = True) #"xform" para obteción de rotaciónn de manera en cola
    cmds.select(clear=True) #Limpiar selección para crear Joints
    rivetJnt = cmds.joint (name=("rivetJoint_"+sel[i]), o=(0,0,0), p=(0,0,0)) #Crear Joint en el origen con prefijo "rivetJoint_" más nombre de Rivet Seleccionado
    cmds.xform (rivetJnt, worldSpace = True, translation=tra) #"xform" para mover selección con index A a lo obtenido en selección index i
    cmds.select(clear=True) #Limpiar selección para emparentar
    cmds.parentConstraint(sel[i], rivetJnt) #Emparentamiento de Rivet maestro a Joint esclavo

#Fin de script

