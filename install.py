from . import SCP_vSingleFile as scp
import imp

imp.reload(scp)

#------------------------------------------------------------------------------------------------------
#Initialize menu window
#------------------------------------------------------------------------------------------------------
def start():
    widget = scp.SCPmain()
    widget.show()

widget = scp.SCPmain()
widget.show()