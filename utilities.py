import maya.cmds as cmds
import curves as cur
import utilities as ut


MESH = "mesh"  #maya node name const
CAM = "camera" #maya node name const
TRANSFORM = "transform" #maya node name const


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
    #A class function that builds a camera rig on selected camera.
    #Return Void
#------------------------------------------------------------------------------------------------------
def U_CameraRig(cam):
        selectedCam = cam
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
        cmds.parent(locatorEmpty, innerLayer)
        cmds.parent(bulbEmpty, innerLayer)

        constraint = cmds.aimConstraint(locator, selectedCam, mo = 1)

        cmds.select(bulb)
        cmds.addAttr(attributeType = "float", defaultValue = 1.0, softMaxValue = 1.0, softMinValue = 0.0, longName = "Aim_Switch", keyable = 1)
        cmds.connectAttr(bulb + ".Aim_Switch", constraint[0] + ".Aimer_ctrlW0")
        cmds.connectAttr(bulb + ".Aim_Switch", locator + ".visibility")
        return
