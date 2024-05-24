import maya.cmds as cmds
import os
import sys
from PySide2 import QtCore, QtWidgets, QtGui

class blendColors(QtWidgets.QWidget):
    def __init__(self):
        self.FKList = None
        self.IKList = None
        self.BlendList = None
        self.BlendCtrl = None

        super().__init__()
        self.setWindowTitle("Blend Color Setup")
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowStaysOnTopHint)


        self.IKJointsList = QtWidgets.QLabel(" ")
        self.selectIKButton = QtWidgets.QPushButton("Select IK joints")

        self.FKJointsList = QtWidgets.QLabel(" ")
        self.selectFKButton = QtWidgets.QPushButton("Select FK joints")

        self.blendJointsList = QtWidgets.QLabel(" ")
        self.selectBlendButton = QtWidgets.QPushButton("Select Blend joints")

        self.blendCtrlList = QtWidgets.QLabel(" ")
        self.selectCtrlButton = QtWidgets.QPushButton("Select blend Control curve")
        self.blendAttrText = QtWidgets.QLabel("Input attr name on ctrl:")
        self.blendAttrName = QtWidgets.QLineEdit()

        self.turnOffSSCButton = QtWidgets.QPushButton("Turn off all segement scale compensate on selected joints")
        self.turnOffSSCButton.released.connect(self.turnOffSSC)

        self.startButton = QtWidgets.QPushButton("Go")

        layoutT = QtWidgets.QVBoxLayout(alignment = QtCore.Qt.AlignCenter)
        layoutT.addWidget(self.IKJointsList)
        layoutT.addWidget(self.selectIKButton)
        self.selectIKButton.released.connect(self.selectIK)
        layoutT.addWidget(self.FKJointsList)
        layoutT.addWidget(self.selectFKButton)
        self.selectFKButton.released.connect(self.selectFK)
        layoutT.addWidget(self.blendJointsList)
        layoutT.addWidget(self.selectBlendButton)
        self.selectBlendButton.released.connect(self.selectBlend)

        layoutT.addWidget(self.blendCtrlList)
        layoutT.addWidget(self.selectCtrlButton)
        self.selectCtrlButton.released.connect(self.selectCtrl)
        layoutT.addWidget(self.blendAttrText)
        layoutT.addWidget(self.blendAttrName)

        layoutT.addWidget(self.startButton)
        self.startButton.released.connect(self.Go)

        layoutT.addWidget(self.turnOffSSCButton)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addLayout(layoutT)

    def selectIK(self):
        self.IKList = cmds.ls(sl = 1)
        self.IKJointsList.setText("".join(self.IKList))
        self.IKList.sort()
        print(self.IKList)
        return

    def selectFK(self):
        self.FKList = cmds.ls(sl = 1)
        self.FKJointsList.setText("".join(self.FKList))
        self.FKList.sort()
        print(self.FKList)
        return

    def selectBlend(self):
        self.BlendList = cmds.ls(sl = 1)
        self.blendJointsList.setText("".join(self.BlendList))
        self.BlendList.sort()
        print(self.BlendList)
        return
    
    def selectCtrl(self):
        self.BlendCtrl = cmds.ls(sl = 1)
        self.blendCtrlList.setText("".join(self.BlendCtrl))
        return

    def turnOffSSC(self):
        for joint in self.FKList:
            cmds.setAttr(joint+".segmentScaleCompensate", 0)

        for joint in self.IKList:
            cmds.setAttr(joint+".segmentScaleCompensate", 0)
            
        for joint in self.BlendList:
            cmds.setAttr(joint+".segmentScaleCompensate", 0)
        return
    

    def Go(self):
        if(self.BlendList == None or self.IKList == None or self.FKList == None):
            cmds.warning("Please select joints")
            return

        if(len(self.BlendList) == 0 or len(self.IKList) == 0 or len(self.FKList) == 0):
            cmds.warning("Please select joints")
            return

        if(len(self.BlendList) != len(self.IKList) or len(self.BlendList) != len(self.FKList) or len(self.IKList) != len(self.FKList)):
            cmds.warning("Joints numbers are different?")
            return

        try:
            cmds.setAttr(self.BlendCtrl[0] + "." + self.blendAttrName.text(), 0.5)
        except:
            cmds.warning("Attribute name on control cannot be found.")
            return

        jointNum = len(self.BlendList)

        for i in range(0, jointNum):
            TransNodeName = self.BlendList[i] + "_Tran_BlendColor"
            RotateNodeName = self.BlendList[i] + "_Rotate_BlendColor"
            scaleNodeName = self.BlendList[i] + "_Scale_BlendColor"
            cmds.createNode("blendColors", n = TransNodeName)
            cmds.createNode("blendColors", n = RotateNodeName)
            cmds.createNode("blendColors", n = scaleNodeName)

            cmds.connectAttr(TransNodeName+".output", self.BlendList[i]+".translate")
            cmds.connectAttr(RotateNodeName+".output", self.BlendList[i]+".rotate")
            cmds.connectAttr(self.IKList[i]+".translate", TransNodeName+".color1")
            cmds.connectAttr(self.IKList[i]+".rotate", RotateNodeName+".color1")
            cmds.connectAttr(self.FKList[i]+".translate", TransNodeName+".color2")
            cmds.connectAttr(self.FKList[i]+".rotate", RotateNodeName+".color2")

            cmds.connectAttr(scaleNodeName+".output", self.BlendList[i]+".scale")
            cmds.connectAttr(self.IKList[i]+".scale", scaleNodeName+".color1")
            cmds.connectAttr(self.FKList[i]+".scale", scaleNodeName+".color2")

            cmds.connectAttr(self.BlendCtrl[0] + "." + self.blendAttrName.text(), TransNodeName+".blender")
            cmds.connectAttr(self.BlendCtrl[0] + "." + self.blendAttrName.text(), RotateNodeName+".blender")

        return