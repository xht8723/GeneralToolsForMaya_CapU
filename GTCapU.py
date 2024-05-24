from ctypes import alignment
import os
import sys
from PySide6 import QtCore, QtWidgets, QtGui
import maya.cmds as cmds
from . import utilities as ut
from . import curves as cur
from . import triPlaner


MESH = "mesh"  #maya node name const
CAM = "camera" #maya node name const
TRANSFORM = "transform" #maya node name const


#------------------------------------------------------------------------------------------------------
#main menu window class
#------------------------------------------------------------------------------------------------------
class GTCapUmain(QtWidgets.QWidget):
    #constructor
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Smart Camera Placement")
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowStaysOnTopHint)
        self.triWindow = triPlaner.tri()
        
        #Widgets
        self.meshText = QtWidgets.QLabel("Select a mesh as point of interest: ")
        self.meshList = QtWidgets.QComboBox()
        self.meshList.setToolTip('What did the modeler say to the psychologist? \n"My life is a mesh!"')

        self.compoText = QtWidgets.QLabel("Select the composition rule: \nWIP")
        self.compositionList = QtWidgets.QComboBox()
        self.compositionList.setToolTip('What have Illuminati and Golden Ration in common?\n"They are both a myth..."')

        self.camText = QtWidgets.QLabel("Select camera: ")
        self.camList = QtWidgets.QComboBox()
        self.camList.setToolTip("I accidentally washed my father's camera's memory card. He's furious because now all the images are watermarked.")
        self.camText1 = QtWidgets.QLabel("Select camera: ")
        self.camList1 = QtWidgets.QComboBox()
        self.camList1.setToolTip("I accidentally washed my father's camera's memory card. He's furious because now all the images are watermarked.")
        self.camText2 = QtWidgets.QLabel("Select camera: ")
        self.camList2 = QtWidgets.QComboBox()
        self.camList2.setToolTip("I accidentally washed my father's camera's memory card. He's furious because now all the images are watermarked.")

        self.startButton = QtWidgets.QPushButton("Smart placement (WIP)")
        self.startButton.setToolTip("Auto place the camera to the best place according to the settings.")

        self.rigCamButton = QtWidgets.QPushButton("Rig the camera")
        self.rigCamButton.setToolTip("Setup a basic rig to the selected camera. \n Works with an aim camera.")
        self.rigCamButton.released.connect(self.doCameraRig)

        self.easyCutButton = QtWidgets.QPushButton("Easy Camera Cut (WIP)")
        self.easyCutButton.setToolTip("Create a cut for selected camera and give it a translate keyframe at perspective camera's current position. \nWIP")

        self.openTriButton = QtWidgets.QPushButton("Triplaner setup")
        self.openTriButton.released.connect(self.openTri)

        self.delHisButton = QtWidgets.QPushButton("Delete History")
        self.delHisButton.released.connect(ut.deleteHistory)

        self.turnTableButton = QtWidgets.QPushButton("Make a turn table of your model")
        self.turnTableButton.released.connect(self.turnTable)

        self.renameText = QtWidgets.QLabel("Rename the curve/empty (or leave it blank):")
        self.renameZeroOut = QtWidgets.QLineEdit()
        self.zeroOutButton = QtWidgets.QPushButton("Zero out selected object")
        self.zeroOutButton.released.connect(self.sendRename)

        self.matchTransButton = QtWidgets.QPushButton("Match Transform")
        self.matchTransButton.released.connect(ut.matchTransform)

        self.refreshButton = QtWidgets.QPushButton("Refresh dropdown lists")
        self.refreshButton.setToolTip("Refreshment means snacks.\nSo refresh must have meaning of eating.\nBut click this won't get you any cookies.")
        self.refreshButton.released.connect(self.initializeComboBox)

        self.controllerText = QtWidgets.QLabel("Create nurbs curve:")
        self.arrow180Button = QtWidgets.QPushButton("Arrow 180")
        self.arrow180Button.released.connect(cur.arrow180)
        self.arrow360Button = QtWidgets.QPushButton("Arrow 360")
        self.arrow360Button.released.connect(cur.arrow360)
        self.arrowBeltButton = QtWidgets.QPushButton("Arrow Belt")
        self.arrowBeltButton.released.connect(cur.arrowBelt)
        self.arrowBowlButton = QtWidgets.QPushButton("Arrow Bowl")
        self.arrowBowlButton.released.connect(cur.arrowBowl)
        self.arrowCircleButton = QtWidgets.QPushButton("Arrow Circle")
        self.arrowCircleButton.released.connect(cur.arrowCircle)
        self.arrowHalfCircleButton = QtWidgets.QPushButton("Arrow Half Circle")
        self.arrowHalfCircleButton.released.connect(cur.arrowHalfCircle)
        self.arrowMultiBurstButton = QtWidgets.QPushButton("Arrow MultiBurst")
        self.arrowMultiBurstButton.released.connect(cur.arrowMultiBurst)
        self.arrowStraightButton = QtWidgets.QPushButton("Arrow Straight")
        self.arrowStraightButton.released.connect(cur.arrowStraight)
        self.arrowWheelButton = QtWidgets.QPushButton("Arrow Wheel")
        self.arrowWheelButton.released.connect(cur.arrowWheel)
        self.ballArrowsButton = QtWidgets.QPushButton("Ball Arrow")
        self.ballArrowsButton.released.connect(cur.ballArrows)
        self.CircleButton = QtWidgets.QPushButton("Circle")
        self.CircleButton.released.connect(cur.circle)
        self.ConeButton = QtWidgets.QPushButton("Cone")
        self.ConeButton.released.connect(cur.cone)
        self.crossButton = QtWidgets.QPushButton("Cross")
        self.crossButton.released.connect(cur.cross)
        self.cubeButton = QtWidgets.QPushButton("Cube")
        self.cubeButton.released.connect(cur.cube)
        self.eightArrowButton = QtWidgets.QPushButton("Eight Arrow")
        self.eightArrowButton.released.connect(cur.eightArrow)
        self.cylinderButton = QtWidgets.QPushButton("Cylinder")
        self.cylinderButton.released.connect(cur.cylinder)
        self.dumbellButton = QtWidgets.QPushButton("Dumbell")
        self.dumbellButton.released.connect(cur.dumbell)
        self.eyeButton = QtWidgets.QPushButton("Eye")
        self.eyeButton.released.connect(cur.eye)
        self.footButton = QtWidgets.QPushButton("Foot")
        self.footButton.released.connect(cur.foot)
        self.handButton = QtWidgets.QPushButton("Hand")
        self.handButton.released.connect(cur.hand)
        self.hitachiButton = QtWidgets.QPushButton("Hitachi")
        self.hitachiButton.released.connect(cur.hitachi)
        self.jackButton = QtWidgets.QPushButton("Jack")
        self.jackButton.released.connect(cur.jack)
        self.keyButton = QtWidgets.QPushButton("Key")
        self.keyButton.released.connect(cur.key)
        self.locatorButton = QtWidgets.QPushButton("Locator(curve)")
        self.locatorButton.released.connect(cur.locator)
        self.nasalStripButton = QtWidgets.QPushButton("Nasal Strip")
        self.nasalStripButton.released.connect(cur.nasalStrip)
        self.pinArrowButton = QtWidgets.QPushButton("Pin Arrow")
        self.pinArrowButton.released.connect(cur.pinArrow)
        self.pinCircleButton = QtWidgets.QPushButton("Pin Circle")
        self.pinCircleButton.released.connect(cur.pinCircle)
        self.pinStarburstButton = QtWidgets.QPushButton("Pin Starburst")
        self.pinStarburstButton.released.connect(cur.pinStarBurst)
        self.pyramidButton = QtWidgets.QPushButton("Pyriamid")
        self.pyramidButton.released.connect(cur.pyramid)
        self.shoulderButton = QtWidgets.QPushButton("Shoulder")
        self.shoulderButton.released.connect(cur.shoulder)
        self.slideBackButton = QtWidgets.QPushButton("Slide back")
        self.slideBackButton.released.connect(cur.slideback)
        self.slideKnobButton = QtWidgets.QPushButton("Slide Knob")
        self.slideKnobButton.released.connect(cur.slideKnob)
        self.sphereHalfButton = QtWidgets.QPushButton("Sphere Half")
        self.sphereHalfButton.released.connect(cur.sphereHalf)
        self.sphereButton = QtWidgets.QPushButton("Sphere")
        self.sphereButton.released.connect(cur.sphere)
        self.spiralButton = QtWidgets.QPushButton("Spiral")
        self.spiralButton.released.connect(cur.spiral)
        self.squareButton = QtWidgets.QPushButton("Squre")
        self.squareButton.released.connect(cur.square)
        self.sunDialButton = QtWidgets.QPushButton("Sun Dial")
        self.sunDialButton.released.connect(cur.sunDial)
        self.sunButton = QtWidgets.QPushButton("Sun")
        self.sunButton.released.connect(cur.sun)
        self.thinArrowButton = QtWidgets.QPushButton("Thin Arrow")
        self.thinArrowButton.released.connect(cur.thinArrow)
        self.wingButton = QtWidgets.QPushButton("Wing")
        self.wingButton.released.connect(cur.wing)
        self.wireArrow180Button = QtWidgets.QPushButton("Wire Arrow 180")
        self.wireArrow180Button.released.connect(cur.wireArrow180)
        self.wireArrowBluntButton = QtWidgets.QPushButton("Wire Arrow Blunt")
        self.wireArrowBluntButton.released.connect(cur.wireArrowBlunt)
        self.wireArrowCircleButton = QtWidgets.QPushButton("Wire Arrow Circle")
        self.wireArrowCircleButton.released.connect(cur.wireArrowCircle)
        self.wireArrowDialButton = QtWidgets.QPushButton("Wire Arrow Dial")
        self.wireArrowDialButton.released.connect(cur.wireArrowDial)
        self.wireArrowTipsButton = QtWidgets.QPushButton("Wire Arrow Tips")
        self.wireArrowTipsButton.released.connect(cur.wireArrowTips)
        self.wireCircleLocatorButton = QtWidgets.QPushButton("Wire Circle Locator")
        self.wireCircleLocatorButton.released.connect(cur.wireCircleLocator)
        self.wireFullCompassButton = QtWidgets.QPushButton("Wire Full Compass")
        self.wireFullCompassButton.released.connect(cur.wireFullCompass)
        self.wireThinArrowButton = QtWidgets.QPushButton("Wire Thin Arrow")
        self.wireThinArrowButton.released.connect(cur.wireThinArrow)
        self.wireTransformButton = QtWidgets.QPushButton("Wire Transform")
        self.wireTransformButton.released.connect(cur.wireTransform)
        self.bulbButton = QtWidgets.QPushButton("Bulb")
        self.bulbButton.released.connect(cur.Bulb)


        #creating tabs
        tabs = QtWidgets.QTabWidget()
        animationTab = QtWidgets.QWidget()
        riggingTab = QtWidgets.QWidget()
        modelingTab = QtWidgets.QWidget()
        tabs.addTab(riggingTab, "Rigging")
        tabs.addTab(modelingTab, "Modeling")
        tabs.addTab(animationTab, "Animation(WIP)")



        #Rigging tab Layout
        vRiggingLayout = QtWidgets.QVBoxLayout(alignment = QtCore.Qt.AlignCenter)
        hRiggingLayout = QtWidgets.QHBoxLayout(alignment = QtCore.Qt.AlignCenter)

        hRiggingLayout.addWidget(self.camText)
        hRiggingLayout.addWidget(self.camList)
        hRiggingLayout.addWidget(self.rigCamButton)

        controllerLayout = QtWidgets.QGridLayout()
        controllerLayout.addWidget(self.controllerText, 0, 0, alignment = QtCore.Qt.AlignBottom)
        controllerLayout.addWidget(self.arrow180Button, 1, 0)
        controllerLayout.addWidget(self.arrow360Button, 1, 1)
        controllerLayout.addWidget(self.arrowBeltButton, 1, 2)
        controllerLayout.addWidget(self.arrowBowlButton, 1, 3)
        controllerLayout.addWidget(self.arrowCircleButton, 1, 4)

        controllerLayout.addWidget(self.arrowHalfCircleButton, 2, 0)
        controllerLayout.addWidget(self.arrowMultiBurstButton, 2, 1)
        controllerLayout.addWidget(self.arrowStraightButton, 2, 2)
        controllerLayout.addWidget(self.arrowWheelButton, 2, 3)
        controllerLayout.addWidget(self.ballArrowsButton, 2, 4)

        controllerLayout.addWidget(self.CircleButton, 3, 0)
        controllerLayout.addWidget(self.ConeButton, 3, 1)
        controllerLayout.addWidget(self.crossButton, 3, 2)
        controllerLayout.addWidget(self.cubeButton, 3, 3)
        controllerLayout.addWidget(self.eightArrowButton, 3, 4)

        controllerLayout.addWidget(self.cylinderButton, 4, 0)
        controllerLayout.addWidget(self.dumbellButton, 4, 1)
        controllerLayout.addWidget(self.eyeButton, 4, 2)
        controllerLayout.addWidget(self.footButton, 4, 3)
        controllerLayout.addWidget(self.handButton, 4, 4)

        controllerLayout.addWidget(self.hitachiButton, 5, 0)
        controllerLayout.addWidget(self.jackButton, 5, 1)
        controllerLayout.addWidget(self.keyButton, 5, 2)
        controllerLayout.addWidget(self.locatorButton, 5, 3)
        controllerLayout.addWidget(self.nasalStripButton, 5, 4)

        controllerLayout.addWidget(self.pinArrowButton, 6, 0)
        controllerLayout.addWidget(self.pinCircleButton, 6, 1)
        controllerLayout.addWidget(self.pinStarburstButton, 6, 2)
        controllerLayout.addWidget(self.pyramidButton, 6, 3)
        controllerLayout.addWidget(self.shoulderButton, 6, 4)

        controllerLayout.addWidget(self.slideBackButton, 7, 0)
        controllerLayout.addWidget(self.slideKnobButton, 7, 1)
        controllerLayout.addWidget(self.sphereHalfButton, 7, 2)
        controllerLayout.addWidget(self.sphereButton, 7, 3)
        controllerLayout.addWidget(self.spiralButton, 7, 4)

        controllerLayout.addWidget(self.squareButton, 8, 0)
        controllerLayout.addWidget(self.sunDialButton, 8, 1)
        controllerLayout.addWidget(self.sunButton, 8, 2)
        controllerLayout.addWidget(self.thinArrowButton, 8, 3)
        controllerLayout.addWidget(self.wingButton, 8, 4)

        controllerLayout.addWidget(self.wireArrow180Button, 9, 0)
        controllerLayout.addWidget(self.wireArrowBluntButton, 9, 1)
        controllerLayout.addWidget(self.wireArrowCircleButton, 9 ,2)
        controllerLayout.addWidget(self.wireArrowDialButton, 9, 3)
        controllerLayout.addWidget(self.wireArrowTipsButton, 9, 4)

        controllerLayout.addWidget(self.wireCircleLocatorButton, 10, 0)
        controllerLayout.addWidget(self.wireFullCompassButton, 10, 1)
        controllerLayout.addWidget(self.wireThinArrowButton, 10, 2)
        controllerLayout.addWidget(self.wireTransformButton, 10, 3)
        controllerLayout.addWidget(self.bulbButton, 10, 4)

        controllerLayout.setContentsMargins(0,50,0,50)

        vRiggingLayout.addLayout(hRiggingLayout)
        vRiggingLayout.addLayout(controllerLayout)

        renameHlayout = QtWidgets.QHBoxLayout(alignment = QtCore.Qt.AlignCenter)
        renameHlayout.addWidget(self.renameText, alignment = QtCore.Qt.AlignCenter)
        renameHlayout.addWidget(self.renameZeroOut, alignment = QtCore.Qt.AlignCenter)
        renameHlayout.addWidget(self.zeroOutButton, alignment = QtCore.Qt.AlignCenter)
        vRiggingLayout.addLayout(renameHlayout)
        vRiggingLayout.addWidget(self.matchTransButton, alignment = QtCore.Qt.AlignCenter)

        riggingTab.setLayout(vRiggingLayout)

        #Animation tab Layout
        vAnimationLayout = QtWidgets.QVBoxLayout(alignment = QtCore.Qt.AlignCenter)
        hAnimationLayout = QtWidgets.QHBoxLayout(alignment = QtCore.Qt.AlignCenter)

        hAnimationLayout.addWidget(self.camText1, alignment = QtCore.Qt.AlignRight)
        hAnimationLayout.addWidget(self.camList1)
        hAnimationLayout.addWidget(self.easyCutButton)

        animationTab.setLayout(hAnimationLayout)


        #Modeling tab Layout
        vModelingLayout = QtWidgets.QVBoxLayout(alignment = QtCore.Qt.AlignCenter)
        hModelingLayout = QtWidgets.QHBoxLayout(alignment = QtCore.Qt.AlignCenter)
        hModelingLayout2 = QtWidgets.QHBoxLayout(alignment = QtCore.Qt.AlignCenter)

        hModelingLayout.addWidget(self.meshText, alignment = QtCore.Qt.AlignRight)
        hModelingLayout.addWidget(self.meshList)

        hModelingLayout2.addWidget(self.camText2, alignment = QtCore.Qt.AlignRight)
        hModelingLayout2.addWidget(self.camList2)

        vModelingLayout.addWidget(self.openTriButton)
        vModelingLayout.addWidget(self.delHisButton)

        hModelingLayout.setContentsMargins(0, 50, 0, 0)
        vModelingLayout.addLayout(hModelingLayout)
        vModelingLayout.addLayout(hModelingLayout2)
        vModelingLayout.addWidget(self.turnTableButton)

        modelingTab.setLayout(vModelingLayout)

        
        #Main Layout
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(tabs)
        self.layout.addWidget(self.refreshButton, alignment = QtCore.Qt.AlignCenter)
        
        #Add dropList items
        self.initializeComboBox()
        
#------------------------------------------------------------------------------------------------------
    #A class function updates all the combobox.
    #Return Void
#------------------------------------------------------------------------------------------------------
    def initializeComboBox(self):
        self.meshList.clear()
        self.camList.clear()
        self.camList1.clear()
        self.camList2.clear()
        self.compositionList.clear()

        self.compositionList.addItem("Rule of 3rd")
        self.compositionList.addItem("Golden Ratio")
        self.compositionList.addItem("Dominant")

        lsOfmesh = ut.lsAll()
        for mesh in lsOfmesh:
            self.meshList.addItem(mesh)
        
        lsOfCam = ut.lsAll(CAM)
        for cam in lsOfCam:
            self.camList.addItem(cam)
            self.camList1.addItem(cam)
            self.camList2.addItem(cam)
        return


#------------------------------------------------------------------------------------------------------
    #get current camera selection
    #Return camera
#------------------------------------------------------------------------------------------------------
    def doCameraRig(self):
        return ut.U_CameraRig(self.camList.currentText())

#------------------------------------------------------------------------------------------------------
    #pass parameters to utility function: doturntable
#------------------------------------------------------------------------------------------------------
    def turnTable(self):
        POI = self.meshList.currentText()
        cam = self.camList2.currentText()
        ut.doTurnTable(cam, POI)
        return

#------------------------------------------------------------------------------------------------------
    #pass parameters to utility function: zeroOut
#------------------------------------------------------------------------------------------------------
    def sendRename(self):
        name = self.renameZeroOut.text()
        if name != "":
            ut.zeroOut(self.renameZeroOut, name)
            return
        ut.zeroOut(self.renameZeroOut)
        return

#------------------------------------------------------------------------------------------------------
    #open the triplaner window
#------------------------------------------------------------------------------------------------------
    def openTri(self):
        self.triWindow.show()

#--------------------------------------script over---------------------------------------------