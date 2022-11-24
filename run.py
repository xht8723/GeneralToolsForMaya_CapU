from . import GTCapU
from . import triPlaner
from . import utilities
from . import curves
import imp

imp.reload(GTCapU)
imp.reload(triPlaner)
imp.reload(utilities)
imp.reload(curves)

#------------------------------------------------------------------------------------------------------
#Initialize menu window
#------------------------------------------------------------------------------------------------------
def start():
    widget = GTCapU.GTCapUmain()
    widget.show()

widget = GTCapU.GTCapUmain()
widget.show()