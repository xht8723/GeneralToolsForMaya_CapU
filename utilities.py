import maya.cmds as cmds
from . import curves as cur
from . import utilities as ut
from pathlib import Path


MESH = "mesh"  #maya node name const
CAM = "camera" #maya node name const
TRANSFORM = "transform" #maya node name const
TURNTABLE = "SCP_turnTable" #turntable mesh name const


#------------------------------------------------------------------------------------------------------
#Utility function that list all objects in the scene that matches the type(Defualt mesh).
#Return a list of strings of names of the objects.
#------------------------------------------------------------------------------------------------------
def lsAll(targetType = MESH):
    if targetType != MESH:
        if targetType != CAM:
            return
        camList = cmds.ls(exactType = CAM)
        return camList
    meshList = cmds.ls(exactType = MESH)
    return meshList


#------------------------------------------------------------------------------------------------------
#Utility function that take a list of shapes and return a list of their corresponding transforms.
#Return a list of strings of names of the transforms.
#------------------------------------------------------------------------------------------------------
def shape2Transform(aList):
    resultList = []
    for item in aList:
        resultList.append(cmds.listRelatives(item, parent = 1))
    return resultList
        

#------------------------------------------------------------------------------------------------------
#Utility function that select all object matches the type.(default mesh)
#    &&&   WIP   &&&
#------------------------------------------------------------------------------------------------------
def selectAll(targetType = MESH):
    if targetType != MESH:
        return

#------------------------------------------------------------------------------------------------------
    #Create an empty group to zero out channels of selected object
    #Return Void
#------------------------------------------------------------------------------------------------------
def zeroOut(textBox, name = None):
    if(name != None):
        sl = cmds.ls(selection = 1)[0]
        cmds.rename(sl, name)
        emp = cmds.group(em = 1, n = name + "Os")
        cmds.matchTransform(emp, name)
        cmds.parent(name, emp)
        textBox.clear()
        return

    sl = cmds.ls(selection = 1)[0]
    emp = cmds.group(em = 1, n = sl + "Os")
    cmds.matchTransform(emp, sl)
    cmds.parent(sl, emp)
    return

#------------------------------------------------------------------------------------------------------
    #Simple match transform with button click
    #Return Void
#------------------------------------------------------------------------------------------------------
def matchTransform():
    from_ = cmds.ls(selection = 1)[0]
    to_ = cmds.ls(selection = 1)[1]
    cmds.matchTransform(from_, to_)
    return

#------------------------------------------------------------------------------------------------------
    #Import the file in the path
    #Return name of the file
#------------------------------------------------------------------------------------------------------
def importModel(path):
    return cmds.file(path, i = 1, mnc = 1)
    
#------------------------------------------------------------------------------------------------------
    #quick button to delete history
    #Return name of the file
#------------------------------------------------------------------------------------------------------
def deleteHistory():
    return cmds.delete(ch = 1)

#------------------------------------------------------------------------------------------------------
    #Create a turntable of selected model and camera
    #Return name of the file
#------------------------------------------------------------------------------------------------------
def doTurnTable(cam, target):
    tablePath = __file__
    tablePath = tablePath.replace("utilities.py", "SCP_turnTable_mesh.fbx")
    importModel(tablePath)

    tgtBBox = cmds.exactWorldBoundingBox(target)
    minX = tgtBBox[0]
    minY = tgtBBox[1]
    minZ = tgtBBox[2]
    maxX = tgtBBox[3]
    maxY = tgtBBox[4]
    maxZ = tgtBBox[5]

    midX = tgtBBox[3] - tgtBBox[0]
    midY = tgtBBox[4] - tgtBBox[1]
    midZ = tgtBBox[5] - tgtBBox[2]

    cmds.setAttr(TURNTABLE+".translateX", minX + midX/2)
    cmds.setAttr(TURNTABLE+".translateY", minY - 28)
    cmds.setAttr(TURNTABLE+".translateZ", minZ + midZ/2)
    U_CameraRig(cam)


    tempGroup = cmds.group(em = 1, n = "temp")
    cmds.setAttr(tempGroup+".translateX", minX + midX/2)
    cmds.setAttr(tempGroup+".translateY", minY + midY/2)
    cmds.setAttr(tempGroup+".translateZ", minZ + midZ/2)

    cmds.matchTransform("camera1_OuterLayer_ctrl", tempGroup, pos = 1)
    cmds.move(midX/2*5, midY/2, midZ/2*5, "camera1_MiddleLayer_ctrl", a = 1)

    cmds.matchTransform("Aimer_ctrl", tempGroup)
    cmds.delete(tempGroup)

    cmds.setKeyframe("camera1_OuterLayer_ctrl", t = 1, itt = "linear", ott = "linear")
    cmds.setAttr("camera1_OuterLayer_ctrl.rotateZ", 420)
    cmds.setKeyframe("camera1_OuterLayer_ctrl", t = 216, itt = "linear", ott = "linear")
    return

#------------------------------------------------------------------------------------------------------
    #A function that builds a camera rig on selected camera.
    #Return Void
#------------------------------------------------------------------------------------------------------
def U_CameraRig(cam):
    selectedCam = cmds.listRelatives(cam, parent = 1)[0]
    camScaleX = cmds.getAttr(selectedCam + ".sx")
    camScaleY = cmds.getAttr(selectedCam + ".sy")
    camScaleZ = cmds.getAttr(selectedCam + ".sz")
    camRotationX = cmds.getAttr(selectedCam + ".rx")
    camRotationY = cmds.getAttr(selectedCam + ".ry")
    camRotationZ = cmds.getAttr(selectedCam + ".rz")

    outerLayer = cmds.circle(name = selectedCam + "_OuterLayer_ctrl")[0]
    midLayer = cmds.circle(name = selectedCam + "_MiddleLayer_ctrl")[0]
    innerLayer = cmds.circle(name = selectedCam + "_InnerLayer_ctrl")[0]
    outerEmpty = cmds.group(em = 1, n = outerLayer + "Os")
    midEmpty = cmds.group(em = 1, n = midLayer + "Os")
    innerEmpty = cmds.group(em = 1, n = innerLayer + "Os")
    bulb = cur.Bulb()
    bulb = cmds.rename(bulb, "Switches_ctrl")
    bulbEmpty = cmds.group(em = 1, n = bulb + "Os")
    locator = cur.wireCircleLocator()
    locator = cmds.rename(locator, "Aimer_ctrl")
    locatorEmpty = cmds.group(em = 1, n = locator + "Os")

    cmds.parent(outerLayer, outerEmpty)
    cmds.parent(midLayer, midEmpty)
    cmds.parent(innerLayer, innerEmpty)
    cmds.parent(locator, locatorEmpty)
    cmds.parent(bulb, bulbEmpty)

    cmds.matchTransform([outerEmpty, midEmpty, innerEmpty, locatorEmpty, bulbEmpty], selectedCam)

    cmds.scale(camScaleX*2, camScaleY*2, camScaleZ*2, innerEmpty)
    cmds.scale(camScaleX*2.5, camScaleY*2.5, camScaleZ*2.5, midEmpty)
    cmds.scale(camScaleX*3, camScaleY*3, camScaleZ*3, outerEmpty)
    cmds.scale(camScaleX*0.15, camScaleY*0.15, camScaleZ*0.15, locatorEmpty)
    cmds.scale(camScaleX*0.5, camScaleY*0.5, camScaleZ*0.5, bulbEmpty)

    cmds.rotate(camRotationX,camRotationY,camRotationZ,locatorEmpty)
    cmds.move(-camScaleX*6, locatorEmpty, os = 1, z = 1, wd = 1)
    cmds.move(camScaleX*5, bulbEmpty, ws = 1, y = 1, wd = 1)
    cmds.rotate(90, 0, 0, [outerEmpty, midEmpty, innerEmpty])

    cmds.parent(midEmpty, outerLayer)
    cmds.parent(innerEmpty, midLayer)
    cmds.parent(selectedCam, innerLayer)
    cmds.parent(locatorEmpty, outerEmpty)
    cmds.parent(bulbEmpty, innerLayer)

    constraint = cmds.aimConstraint(locator, selectedCam, mo = 1, aim = [0, 0, -1])

    cmds.select(bulb)
    cmds.addAttr(attributeType = "float", defaultValue = 1.0, softMaxValue = 1.0, softMinValue = 0.0, longName = "Aim_Switch", keyable = 1)
    cmds.connectAttr(bulb + ".Aim_Switch", constraint[0] + ".Aimer_ctrlW0")
    cmds.connectAttr(bulb + ".Aim_Switch", locator + ".visibility")
    return
