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
        #creating tabs layout
        tabs = QtWidgets.QTabWidget()
        animationTab = QtWidgets.QWidget()
        riggingTab = QtWidgets.QWidget()
        modelingTab = QtWidgets.QWidget()
        tabs.addTab(riggingTab, "Rigging")
        tabs.addTab(animationTab, "Animation")
        tabs.addTab(modelingTab, "Modeling")
        
        #Widgets
        self.POIText = QtWidgets.QLabel("Select a mesh as point of interest: ")
        self.meshList = QtWidgets.QComboBox()
        self.meshList.setToolTip('What did the modeler say to the psychologist? \n"My life is a mesh!"')


        self.compoText = QtWidgets.QLabel("Select the composition rule: \nWIP")
        self.compositionList = QtWidgets.QComboBox()
        self.compositionList.setToolTip('What have Illuminati and Golden Ration in common?\n"They are both a myth..."')


        self.camText = QtWidgets.QLabel("Select camera: ")
        self.camList = QtWidgets.QComboBox()
        self.camList.setToolTip("I accidentally washed my father's camera's memory card. He's furious because now all the images are watermarked.")


        self.startButton = QtWidgets.QPushButton("Smart placement (WIP)")
        self.startButton.setToolTip("Auto place the camera to the best place according to the settings.")


        self.rigCamButton = QtWidgets.QPushButton("Rig the camera")
        self.rigCamButton.setToolTip("Setup a basic rig to the selected camera. \n Works with an aim camera.")


        self.easyCutButton = QtWidgets.QPushButton("Easy Camera Cut (WIP)")
        self.easyCutButton.setToolTip("Create a cut for selected camera and give it a translate keyframe at perspective camera's current position. \nWIP")


        self.refreshButton = QtWidgets.QPushButton("Refresh dropdown lists")
        self.refreshButton.setToolTip("Refreshment means snacks.\nSo refresh must have meaning of eating.\nBut click this won't get you any cookies.")

        self.arrow180Button = QtWidgets.QPushButton("Arrow 180")
        self.arrow180Button.released.connect(self.arrow180)
        self.arrow360Button = QtWidgets.QPushButton("Arrow 360")
        self.arrow360Button.released.connect(self.arrow360)
        self.arrowBeltButton = QtWidgets.QPushButton("Arrow Belt")
        self.arrowBeltButton.released.connect(self.arrowBelt)
        self.arrowBowlButton = QtWidgets.QPushButton("Arrow Bowl")
        self.arrowBowlButton.released.connect(self.arrowBowl)
        self.arrowCircleButton = QtWidgets.QPushButton("Arrow Circle")
        self.arrowHalfCircleButton = QtWidgets.QPushButton("Arrow Half Circle")
        self.arrowMultiBurstButton = QtWidgets.QPushButton("Arrow MultiBurst")
        self.arrowStraightButton = QtWidgets.QPushButton("Arrow Straight")
        self.arrowWheelButton = QtWidgets.QPushButton("Arrow Wheel")
        self.ballArrowsButton = QtWidgets.QPushButton("Ball Arrow")
        self.CircleButton = QtWidgets.QPushButton("Circle")
        self.ConeButton = QtWidgets.QPushButton("Cone")
        self.crossButton = QtWidgets.QPushButton("Cross")
        self.cubeButton = QtWidgets.QPushButton("Cube")
        self.eightArrowButton = QtWidgets.QPushButton("Eight Arrow")
        self.cylinderButton = QtWidgets.QPushButton("Cylinder")
        self.dumbellButton = QtWidgets.QPushButton("Dumbell")
        self.eyeButton = QtWidgets.QPushButton("Eye")
        self.footButton = QtWidgets.QPushButton("Foot")
        self.handButton = QtWidgets.QPushButton("Hand")
        self.hitachiButton = QtWidgets.QPushButton("Hitachi")
        self.jackButton = QtWidgets.QPushButton("Jack")
        self.keyButton = QtWidgets.QPushButton("Key")
        self.locatorButton = QtWidgets.QPushButton("Locator(curve)")
        self.nasalStripButton = QtWidgets.QPushButton("Nasal Strip")
        self.pinArrowButton = QtWidgets.QPushButton("Pin Arrow")
        self.pinCircleButton = QtWidgets.QPushButton("Pin Circle")
        self.pinStarburstButton = QtWidgets.QPushButton("Pin Starburst")
        self.pyramidButton = QtWidgets.QPushButton("Pyriamid")
        self.shoulderButton = QtWidgets.QPushButton("Shoulder")
        self.slideBackButton = QtWidgets.QPushButton("Slide back")
        self.slideKnobButton = QtWidgets.QPushButton("Slide Knob")
        self.sphereHalfButton = QtWidgets.QPushButton("Sphere Half")
        self.sphereButton = QtWidgets.QPushButton("Sphere")
        self.spiralButton = QtWidgets.QPushButton("Spiral")
        self.squreButton = QtWidgets.QPushButton("Squre")
        self.sunDialButton = QtWidgets.QPushButton("Sun Dial")
        self.sunButton = QtWidgets.QPushButton("Sun")
        self.thinArrowButton = QtWidgets.QPushButton("Thin Arrow")
        self.wingButton = QtWidgets.QPushButton("Wing")
        self.wireArrow180Button = QtWidgets.QPushButton("Wire Arrow 180")
        self.wireArrowBluntButton = QtWidgets.QPushButton("Wire Arrow Blunt")
        self.wireArrowDialButton = QtWidgets.QPushButton("Wire Arrow Dial")
        self.wireArrowTipsButton = QtWidgets.QPushButton("Wire Arrow Tips")
        self.wireCircleLocatorButton = QtWidgets.QPushButton("Wire Circle Locator")
        self.wireFullCompassButton = QtWidgets.QPushButton("Wire Full Compass")
        self.wireThinArrowButton = QtWidgets.QPushButton("Wire Thin Arrow")
        self.wireTransformButton = QtWidgets.QPushButton("Wire Transform")
        self.bulbButton = QtWidgets.QPushButton("Bulb")




        #Layouts
        hLayoutCompo = QtWidgets.QHBoxLayout(alignment = QtCore.Qt.AlignHCenter)
        hLayoutPOI = QtWidgets.QHBoxLayout(alignment = QtCore.Qt.AlignHCenter)

        
        # hLayoutCompo.addWidget(self.compoText)
        # hLayoutCompo.addWidget(self.compositionList)

        # hLayoutPOI.addWidget(self.POIText)
        # hLayoutPOI.addWidget(self.meshList)

        # hLayoutCam.addWidget(self.camText)
        # hLayoutCam.addWidget(self.camList)
        # hLayoutCam.addWidget(self.rigCamButton)
        # hLayoutCam.addWidget(self.easyCutButton)
        # self.rigCamButton.released.connect(self.doCameraRig)

        #Tabs Layout
        riggingTab.layout = QtWidgets.QVBoxLayout()
        riggingTab.layout.addWidget(self.camText)
        riggingTab.layout.addWidget(self.camList)
        riggingTab.layout.addWidget(self.rigCamButton)

        hRiggingLayout = QtWidgets.QHBoxLayout(alignment = QtCore.Qt.AlignHCenter)
        hRiggingLayout.addWidget(self.camText)
        hRiggingLayout.addWidget(self.camList)
        hRiggingLayout.addWidget(self.rigCamButton)
        # hRiggingLayout.addWidget(self.arrow180Button)
        # hRiggingLayout.addWidget(self.arrow360Button)
        # hRiggingLayout.addWidget(self.arrowBeltButton)
        # hRiggingLayout.addWidget(self.arrowBowlButton)

        controllerLayout = QtWidgets.QVBoxLayout()
        controllerLayout.addWidget(self.arrow180Button)
        controllerLayout.addWidget(self.arrow360Button)
        controllerLayout.addWidget(self.arrowBeltButton)
        controllerLayout.addWidget(self.arrowBowlButton)

        # riggingTab.setLayout(hRiggingLayout)
        # riggingTab.layout.addLayout(controllerLayout)


        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(tabs)
        # self.layout.addLayout(hLayoutCam)
        # self.layout.addLayout(hLayoutPOI)
        # self.layout.addLayout(hLayoutCompo)
        # self.layout.addWidget(self.refreshButton)
        # self.refreshButton.released.connect(self.initializeComboBox)
        # self.layout.addWidget(self.startButton)
        # self.startButton.released.connect(self.SmartCamera)
        

        
        #Updates dropList items
        self.initializeComboBox()
        
        
    

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
#Functions to create curves.
#------------------------------------------------------------------------------------------------------
    def arrow180(self):
        return cmds.curve(d=1, p = [(2.635711045970995, -2.874089854998373e-14, -8.366325043590853), (5.394190551311968, -4.980044154834218e-13, -5.588550353929405), (5.394190551311968, -4.980044154834218e-13, -5.588550353929405), (5.394190551311955, -3.0299374120801303e-13, -13.95016097257651), (5.394190551311955, -3.0299374120801303e-13, -13.95016097257651), (-2.8812479647109894, 9.09813890892508e-13, -13.921874422913778), (-2.8812479647109894, 9.09813890892508e-13, -13.921874422913778), (-0.12276845937000942, 4.405226183834543e-13, -11.144099733252318), (-0.12276845937000942, 4.405226183834543e-13, -11.144099733252318), (-4.118696150600751, 9.091477570777329e-13, -6.1134748440525), (-5.3941905513120645, 9.530570777016578e-13, 0.02273284686891065), (-4.11869615060073, 6.230987947830613e-13, 6.150220918729564), (-0.12276845936997698, -7.953360192658464e-14, 11.153528583139945), (-0.12276845936997698, -7.953360192658464e-14, 11.153528583139945), (-2.8812479647109432, 2.5972279882324756e-13, 13.950160972576565), (-2.8812479647109432, 2.5972279882324756e-13, 13.950160972576565), (5.394190551312003, -9.530570777016578e-13, 13.921874422913826), (5.394190551312003, -9.530570777016578e-13, 13.921874422913826), (5.394190551311987, -7.580464034262491e-13, 5.560263804266727), (5.394190551311987, -7.580464034262491e-13, 5.560263804266727), (2.6357110459710196, -4.1879000267641686e-13, 8.356896193703326), (2.6357110459710196, -4.1879000267641686e-13, 8.356896193703326), (-0.30387953798024286, 8.308631560538517e-14, 5.319601684686134), (-1.6957739750624936, 4.110461970796564e-13, 0.010091167040707498), (-0.3038795379802619, 3.309991170041826e-13, -5.308934711281626), (2.635711045970995, -2.874089854998373e-14, -8.366325043590853)])

    def arrow360(self):
        return cmds.curve(d=1, p = [(-0.01286873565133817, -0.0008085438445470087, 10.016073828221842), (0.0045415231518433075, -0.0008085438445470166, 10.016073828221842), (0.01286873565132396, -0.0008085438445470202, 10.016073828221828), (4.001888008136888, -0.0008085438445470124, 6.0096442969330965), (4.001888008136888, -0.0008085438445470135, 6.011858673871515), (3.9990682525462162, -0.0008085438445470112, 6.0096442969330965), (1.998673242492515, -0.0008085438445461228, 6.0096442969330965), (2.0088063113348156, -0.0008085438445461274, 6.009644296933104), (1.998673242492515, -0.0008085438445461193, 6.001902060401562), (1.9986732424925222, -0.0008085438445443544, 2.0272806506615737), (1.998673242492515, -0.0008085438445443436, 2.0032147656443726), (2.026741368089688, -0.0008085438445443561, 2.0032147656443726), (5.976335191382958, -0.0008085438445461101, 2.0032147656443726), (6.005102773781253, -0.0008085438445461228, 2.0032147656443726), (6.00510277378126, -0.0008085438445461343, 2.0290228862946265), (6.019591633325938, -0.0008085438445470188, 4.006429531288731), (6.005102773781253, -0.0008085438445470077, 3.995893020683397), (6.005102773781253, -0.0008085438445470124, 4.006429531288745), (10.011532305069991, -0.0008085438445470124, 7.105427357601002e-15), (9.993232026827783, -0.0008085438445470107, 0.013991619208937323), (9.999918967664208, 0.0071127120043418925, -0.010448691083190909), (6.017206158816393, -0.0071127120043516555, -4.000301182171423), (6.0051027737812674, -0.0008085438445434539, -4.0064295312887275), (6.00510277378126, -0.0008085438445434588, -3.995570844469249), (6.0051027737812674, -0.0008085438445443436, -2.0032147656443584), (6.00510277378126, -0.0008085438445443397, -2.011848741975001), (5.99177627892503, -0.0008085438445443377, -2.0032147656443584), (1.9986732424925293, -0.0008085438445425644, -2.003214765644362), (1.9986732424925293, -0.000808543844542558, -2.0177898738369286), (2.0119371586016896, -0.0008085438445425703, -2.003214765644369), (2.000096968698834, -0.0008085438445407858, -6.0096442969331), (1.9986732424925293, -0.0008085438445407863, -6.007136762604901), (1.9986732424925293, -0.0008085438445407852, -6.0096442969331), (4.001888008136902, -0.0008085438445416721, -6.016046256349334), (4.001888008136902, -0.0008085438445416748, -6.0096442969331), (3.9852702973795218, -0.0008085438445416675, -6.009644296933104), (0.005965589350537925, 0.0011946073651421909, -10.009166974666684), (0.004541523151850413, -0.0008085438445381205, -10.016073828221842), (-0.005965589350516609, 0.001194607365142196, -10.009166974666684), (-4.001888008136888, -0.0008085438445381177, -6.016046256349341), (-4.001888008136888, -0.0008085438445381205, -6.009644296933107), (-3.9852702973795076, -0.0008085438445381278, -6.009644296933104), (-2.00009696869882, -0.0008085438445390095, -6.009644296933104), (-1.9986732424925222, -0.0008085438445390101, -6.009644296933104), (-1.9986732424925222, -0.0008085438445390112, -6.007136762604908), (-1.9986732424925222, -0.0008085438445407829, -2.0177898738369286), (-1.9986732424925222, -0.0008085438445407893, -2.003214765644369), (-2.0119371586016754, -0.0008085438445407834, -2.003214765644369), (-5.991776278925023, -0.0008085438445390161, -2.0032147656443726), (-6.005102773781257, -0.0008085438445390101, -2.0032147656443726), (-6.005102773781257, -0.0008085438445390063, -2.0118487419750117), (-6.005102773781257, -0.0008085438445381254, -3.9955708444692597), (-6.005102773781257, -0.0008085438445381205, -4.006429531288742), (-6.017206158816386, -0.007112712004346313, -4.000301182171434), (-9.999918967664208, 0.007112712004350775, -0.01044869108320512), (-10.011532305069991, -0.0008085438445381205, -7.105427357601002e-15), (-9.993232026827783, -0.0008085438445381347, 0.013991619208916006), (-6.019591633325945, -0.0008085438445416725, 4.006429531288731), (-6.00510277378126, -0.000808543844541679, 4.006429531288731), (-6.00510277378126, -0.0008085438445416742, 3.99589302068339), (-6.00510277378126, -0.0008085438445408008, 2.0290228862946194), (-6.00510277378126, -0.0008085438445407893, 2.0032147656443726), (-5.976335191382958, -0.000808543844540802, 2.0032147656443726), (-2.026741368089688, -0.000808543844542556, 2.0032147656443726), (-1.9986732424925222, -0.0008085438445425686, 2.0032147656443726), (-1.9986732424925222, -0.0008085438445425793, 2.0272806506615737), (-1.9986732424925222, -0.0008085438445443443, 6.001902060401562), (-1.9986732424925222, -0.0008085438445443478, 6.009644296933104), (-2.0088063113348227, -0.0008085438445443432, 6.009644296933104), (-3.9990682525462233, -0.0008085438445434594, 6.009644296933104), (-4.001888008136895, -0.0008085438445434582, 6.009644296933104), (-4.001888008136895, -0.0008085438445434593, 6.011858673871515)])
 
    def arrowBelt(self):
        return cmds.curve(d=1, p = [(1.9999999999999987, 1.4762479884695947, -8.980823116301465), (1.9999999999999996, -0.8695778098722888, -8.980823116301446), (2.000000000000002, -5.561229406556037, -7.0374773950256), (2.000000000000003, -8.476247988469677, 7.920623077296649e-14), (2.000000000000002, -5.561229406555909, 7.037477395025701), (2.0000000000000013, -0.869577809872125, 8.98082311630146), (1.9999999999999996, 1.47624798846976, 8.98082311630144), (3.6666666666666656, 1.47624798846976, 9.000000000000139), (5.333333333333332, 1.47624798846976, 9.000000000000139), (7.0, 1.47624798846976, 9.000000000000139), (4.666666666666666, 3.809581321803093, 9.000000000000115), (2.3333333333333326, 6.142914655136425, 9.000000000000094), (-8.881784197001252e-16, 8.47624798846976, 9.000000000000073), (-2.333333333333334, 6.142914655136425, 9.000000000000094), (-4.666666666666667, 3.8095813218030927, 9.000000000000115), (-7.0, 1.47624798846976, 9.000000000000139), (-5.333333333333334, 1.47624798846976, 9.000000000000139), (-3.666666666666667, 1.47624798846976, 9.000000000000139), (-2.0000000000000004, 1.47624798846976, 9.000000000000139), (-1.999999999999999, -0.8695778098721245, 8.98082311630146), (-1.9999999999999971, -5.561229406555909, 7.037477395025701), (-1.999999999999996, -8.476247988469678, 7.920623077296651e-14), (-1.9999999999999978, -5.561229406556037, -7.0374773950256), (-2.0, -0.8695778098722888, -8.980823116301446), (-2.000000000000001, 1.4762479884695947, -8.980823116301465), (-3.666666666666667, 1.4762479884695978, -9.000000000000163), (-5.333333333333334, 1.4762479884695978, -9.000000000000163), (-7.0, 1.4762479884695978, -9.000000000000163), (-4.666666666666667, 3.809581321802931, -9.000000000000183), (-2.333333333333334, 6.142914655136264, -9.000000000000204), (-8.881784197001252e-16, 8.476247988469597, -9.000000000000226), (2.3333333333333326, 6.142914655136264, -9.000000000000204), (4.666666666666666, 3.8095813218029315, -9.000000000000183), (7.0, 1.4762479884695978, -9.000000000000163), (5.333333333333332, 1.4762479884695978, -9.000000000000163), (3.6666666666666656, 1.4762479884695978, -9.000000000000163), (1.9999999999999991, 1.4762479884695978, -9.000000000000163)])
    
    def arrowBowl(self):
        return cmds.curve(d=1, p = [(5.431172424626894, 1.72981783677632, 0.03445487012004378), (3.620781616417929, 3.5402086449852845, 0.03445487012004378), (3.620781616417929, 3.5402086449852845, 0.03445487012004378), (9.051954041044837, 3.5402086449852845, 0.034454870120050884), (9.051954041044837, 3.5402086449852845, 0.034454870120050884), (9.051954041044837, -1.8909637796416092, 0.034454870120050884), (9.051954041044837, -1.8909637796416092, 0.034454870120050884), (7.2415632328358654, -0.08057297143264464, 0.03445487012004378), (7.2415632328358654, -0.08057297143264464, 0.03445487012004378), (3.982859839365048, -2.7031013420313315, 0.03445487012004378), (0.0, -3.5402086449852845, 0.03445487012004378), (-3.982859839365048, -2.7031013420313315, 0.03445487012004378), (-7.2415632328358726, -0.08057297143264464, 0.034454870120036674), (-7.2415632328358726, -0.08057297143264464, 0.034454870120036674), (-9.051954041044837, -1.8909637796416092, 0.034454870120036674), (-9.051954041044837, -1.8909637796416092, 0.034454870120036674), (-9.051954041044837, 3.5402086449852845, 0.034454870120036674), (-9.051954041044837, 3.5402086449852845, 0.034454870120036674), (-3.6207816164179434, 3.5402086449852845, 0.034454870120036674), (-3.6207816164179434, 3.5402086449852845, 0.034454870120036674), (-5.431172424626908, 1.72981783677632, 0.034454870120036674), (-5.431172424626908, 1.72981783677632, 0.034454870120036674), (-3.4518118829398077, -0.19943621886513085, 0.03445487012004378), (0.0, -1.112936895600967, 0.03445487012004378), (3.4518118829398077, -0.19943621886513085, 0.03445487012004378), (5.431172424626894, 1.72981783677632, 0.03445487012004378), (0.02398843417912211, 1.72981783677632, 5.431172424626901), (0.023988434179115004, 3.5402086449852845, 3.620781616417929), (0.023988434179115004, 3.5402086449852845, 3.620781616417929), (0.023988434179120333, 3.5402086449852845, 9.051954041044837), (0.023988434179120333, 3.5402086449852845, 9.051954041044837), (0.023988434179120333, -1.8909637796416092, 9.051954041044837), (0.023988434179120333, -1.8909637796416092, 9.051954041044837), (0.023988434179120333, -0.08057297143264464, 7.2415632328358726), (0.023988434179120333, -0.08057297143264464, 7.2415632328358726), (0.02398843417912211, -2.7031013420313315, 3.982859839365048), (0.023988434179123885, -3.5402086449852845, 0.0), (0.023988434179118556, -2.7031013420313315, -3.982859839365048), (0.023988434179120333, -0.08057297143264464, -7.2415632328358654), (0.023988434179120333, -0.08057297143264464, -7.2415632328358654), (0.023988434179120333, -1.8909637796416092, -9.051954041044837), (0.023988434179120333, -1.8909637796416092, -9.051954041044837), (0.023988434179120333, 3.5402086449852845, -9.051954041044837), (0.023988434179120333, 3.5402086449852845, -9.051954041044837), (0.023988434179118556, 3.5402086449852845, -3.6207816164179363), (0.023988434179118556, 3.5402086449852845, -3.6207816164179363), (0.023988434179118556, 1.72981783677632, -5.431172424626894), (0.023988434179118556, 1.72981783677632, -5.431172424626894), (0.023988434179118556, -0.19943621886513085, -3.4518118829398077), (0.02398843417911678, -1.112936895600967, 0.0), (0.02398843417912211, -0.19943621886513085, 3.4518118829398077), (0.02398843417912211, 1.72981783677632, 5.431172424626901)])
 




#------------------------------------------------------------------------------------------------------
#Initialize menu window
#------------------------------------------------------------------------------------------------------
widget = SCPmain()
widget.resize(600, 600)
widget.show()










#--------------------------------------script over---------------------------------------------