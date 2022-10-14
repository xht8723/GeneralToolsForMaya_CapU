import sys
from PySide2 import QtCore, QtWidgets, QtGui
import maya.cmds as cmds

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
#main menu window class
#------------------------------------------------------------------------------------------------------
class SCPmain(QtWidgets.QWidget):


    #constructor
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Smart Camera Placement")
        self.meshList = QtWidgets.QComboBox(self)
        self.meshList.setToolTip('What did the modeler say to the psychologist? \n"My life is a mesh!"')
        self.compositionList = QtWidgets.QComboBox(self)
        self.compositionList.setToolTip('What have Illuminati and Golden Ration in common?\n"They are both a myth..."')
        self.camList = QtWidgets.QComboBox(self)
        self.camList.setToolTip("I accidentally washed my father's camera's memory card. He's furious because now all the images are watermarked.")
        self.startButton = QtWidgets.QPushButton("Smart placement (WIP)")
        self.startButton.setToolTip("Auto place the camera to the best place according to the settings.")
        self.rigCamButton = QtWidgets.QPushButton("Rig the camera")
        self.rigCamButton.setToolTip("Setup a basic rig to the selected camera. \n Works with an aim camera.")
        self.easyCutButton = QtWidgets.QPushButton("Easy Camera Cut (WIP)")
        self.easyCutButton.setToolTip("Create a cut for selected camera and give it a translate keyframe at perspective camera's current position. \nWIP")
        self.refreshButton = QtWidgets.QPushButton("Refresh dropdown lists")
        self.refreshButton.setToolTip("Refreshment means snacks.\nSo refresh must have meaning of eating.\nBut click this won't get you any cookies.")
        self.compoText = QtWidgets.QLabel("Select the composition rule: \nWIP")
        self.POIText = QtWidgets.QLabel("Select a mesh as point of interest: ")
        self.camText = QtWidgets.QLabel("Select camera: ")


        self.initializeComboBox()
        
        #Layouts
        hLayoutCompo = QtWidgets.QHBoxLayout(alignment = QtCore.Qt.AlignHCenter)
        hLayoutPOI = QtWidgets.QHBoxLayout(alignment = QtCore.Qt.AlignHCenter)
        hLayoutCam = QtWidgets.QHBoxLayout(alignment = QtCore.Qt.AlignHCenter)
        
        hLayoutCompo.addWidget(self.compoText)
        hLayoutCompo.addWidget(self.compositionList)

        hLayoutPOI.addWidget(self.POIText)
        hLayoutPOI.addWidget(self.meshList)

        hLayoutCam.addWidget(self.camText)
        hLayoutCam.addWidget(self.camList)
        hLayoutCam.addWidget(self.rigCamButton)
        hLayoutCam.addWidget(self.easyCutButton)
        self.rigCamButton.released.connect(self.doCameraRig)


        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addLayout(hLayoutCam)
        self.layout.addLayout(hLayoutPOI)
        self.layout.addLayout(hLayoutCompo)
        self.layout.addWidget(self.refreshButton)
        self.refreshButton.released.connect(self.initializeComboBox)
        self.layout.addWidget(self.startButton)
        self.startButton.released.connect(self.SmartCamera)
        
    

#------------------------------------------------------------------------------------------------------
    #A class function updates all the combobox.
    #Return Void
#------------------------------------------------------------------------------------------------------
    def initializeComboBox(self):
        self.meshList.clear()
        self.camList.clear()
        self.compositionList.clear()

        self.compositionList.addItem("Rule of 3rd")
        self.compositionList.addItem("Golden Ratio")
        self.compositionList.addItem("Dominant")

        lsOfmesh = lsAll()
        for mesh in lsOfmesh:
            self.meshList.addItem(mesh)
        
        lsOfCam = lsAll(CAM)
        for cam in lsOfCam:
            self.camList.addItem(cam)
        return



#------------------------------------------------------------------------------------------------------
    #A class function that builds a camera rig on selected camera.
    #Return Void
#------------------------------------------------------------------------------------------------------
    def doCameraRig(self):
        selectedCam = cmds.listRelatives(self.camList.currentText(), parent = 1)[0]
        camScaleX = cmds.getAttr(selectedCam + ".sx")
        camScaleY = cmds.getAttr(selectedCam + ".sy")
        camScaleZ = cmds.getAttr(selectedCam + ".sz")

        outerLayer = cmds.circle(name = selectedCam + "_OuterLayer_ctrl")[0]
        midLayer = cmds.circle(name = selectedCam + "_MiddleLayer_ctrl")[0]
        innerLayer = cmds.circle(name = selectedCam + "_InnerLayer_ctrl")[0]
        outerEmpty = cmds.group(em = 1, n = outerLayer + "Os")
        midEmpty = cmds.group(em = 1, n = midLayer + "Os")
        innerEmpty = cmds.group(em = 1, n = innerLayer + "Os")
        # aimLocator = cmds.spaceLocator(name = selectedCam + "_aim_ctrl")[0]
        # aimEmpty = cmds.group(em = 1, n = aimLocator + "Os")

        cmds.matchTransform([outerLayer,midLayer,innerLayer], selectedCam)
        cmds.matchTransform([outerEmpty,midEmpty,innerEmpty], selectedCam)
        # cmds.parent(aimLocator, aimEmpty)
        # cmds.matchTransform(aimEmpty, selectedCam)
        cmds.parent(outerLayer, outerEmpty)
        cmds.parent(midLayer, midEmpty)
        cmds.parent(innerLayer, innerEmpty)

        cmds.scale(camScaleX*2, camScaleY*2, camScaleZ*2, innerEmpty)
        cmds.scale(camScaleX*2.5, camScaleY*2.5, camScaleZ*2.5, midEmpty)
        cmds.scale(camScaleX*3, camScaleY*3, camScaleZ*3, outerEmpty)

        cmds.rotate(90, 0, 0, [outerEmpty, midEmpty, innerEmpty])


        cmds.parent(midEmpty, outerLayer)
        cmds.parent(innerEmpty, midLayer)
        # cmds.parent(aimEmpty, innerLayer)

        # cmds.aimConstraint(aimLocator, selectedCam)


        cmds.parent(selectedCam, innerLayer)



        return
    


#------------------------------------------------------------------------------------------------------
#Algorithm for smart camera placement.
#------------------------------------------------------------------------------------------------------
    def SmartCamera(self):
        #god i haven't done math for so long...
        return


#------------------------------------------------------------------------------------------------------
#Initialize menu window
#------------------------------------------------------------------------------------------------------
widget = SCPmain()
widget.show()










#--------------------------------------script over---------------------------------------------