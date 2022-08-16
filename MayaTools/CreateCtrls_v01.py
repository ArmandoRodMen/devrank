#Create Ctrls v0.1
#Armando Rodriguez 
#Script crear Grupo y Curva en posición de Joint seleccionado

import maya.cmds as cmds #importar biblioteca de maya a python

sel = cmds.ls(selection=True) #crear lista de objetos seleccionados
print sel #se imprime lista de seleccionados

for i in sel: #ciclo "for", denrto de la lista "sel"

#Obtener radio, traslación y rotación de "i"

    rad = cmds.getAttr (i + ".radius") #Mandar a llamar radio
    tra = cmds.xform (i, query=True, worldSpace=True, translation=True) #"xform" para obteción de traslación de manera en cola
    rot = cmds.xform (i, query=True, worldSpace=True, rotation=True) #"xform" para obteción de rotaciónn de manera en cola
    print rad, tra, rot, i #imprimir para comprobar y debug
    
#Crea grupo padre y curva control

    ctr = cmds.circle (normal=(1,0,0), radius=rad*1.25, name="Ctrl_"+i) #crear círculo con normal en X, radio de 1.23 y nombre + i (seleccionado)
    grp = cmds.group (name="Grp_"+i) #Crear grupo + i (seleccionado)
    cmds.select(clear=True) #Limpiar selección
    cmds.setAttr (ctr[0] + ".overrideEnabled",1) #Activar color al circulo controlador
    cmds.setAttr (ctr[0] + ".overrideColor",18) #Agregar color al circulo controlador
    cmds.xform (grp, worldSpace=True, translation=tra) #"xform" para mover selección con index A a lo obtenido en selección index i
    cmds.xform (grp, worldSpace=True, rotation=rot) #"xform" para rotar selección con index A a lo obtenido en selección index i

#Fin de script


