import maya.cmds as cmds
from PySide2 import QtCore, QtWidgets, QtGui

class tri(QtWidgets.QWidget):
    def __init__(self):
        super(tri, self).__init__()

        self.setWindowTitle("Triplanar")
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowStaysOnTopHint)

        self.instruction = QtWidgets.QLabel("Select your images and rsMaterial in the following order: \n\nimage X, image Y, image Z, rsMaterial. Then press the button.\n\n(image Y and Z can be neglected if you wish for same image on each axis)")
        self.goButton = QtWidgets.QPushButton("Connect Triplanar")
        self.goButton.released.connect(self.triplanar)
        self.channels = QtWidgets.QComboBox()

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.channels)
        self.layout.addWidget(self.instruction)
        self.layout.addWidget(self.goButton)

        self.channels.addItem("base_color")
        self.channels.addItem("refl_roughness")
        self.channels.addItem("bump_input")

    def triplanar(self):
        channel = self.channels.currentText()
        channel = "." + channel

        print(channel)

        sl = cmds.ls(selection = 1)


        if len(sl) >= 2:
            rsmat = sl[len(sl)-1]
            sl.pop()
            rsTri = cmds.createNode("RedshiftTriPlanar")

            if channel == ".base_color":
                cmds.connectAttr(rsTri+".outColor", rsmat+channel)
            else:
                cmds.connectAttr(rsTri+".outColorR",rsmat+channel)
            
            count = 0
            for each in sl:

                cmds.setAttr(rsTri+".sameImageOnEachAxis", 1)

                if count > 2:
                    cmds.warning("too many images.")
                    break

                if count == 0:
                    cmds.connectAttr(each+".outColor", rsTri+".imageX")


                if count == 1:
                    cmds.setAttr(rsTri+".sameImageOnEachAxis", 0)
                    cmds.connectAttr(each+".outColor", rsTri+".imageY")


                if count == 2:
                    cmds.connectAttr(each+".outColor", rsTri+".imageZ")

                count = count + 1


        else:
            cmds.warning("Please select your image nodes and red shift material node.")

        return