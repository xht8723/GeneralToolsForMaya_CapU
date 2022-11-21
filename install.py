from . import SCP_vSingleFile as scp
from . import triPlaner
from . import utilities
from . import curves
import imp

imp.reload(scp)
imp.reload(triPlaner)
imp.reload(utilities)
imp.reload(curves)

#------------------------------------------------------------------------------------------------------
#Initialize menu window
#------------------------------------------------------------------------------------------------------
def start():
    widget = scp.SCPmain()
    widget.show()

widget = scp.SCPmain()
widget.show()