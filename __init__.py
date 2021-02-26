from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


import anim_picker.core.gui as anim_picker_gui


__version__ = "1.3.1"


# =============================================================================
# Load user interface function
# =============================================================================
def load(edit=False, dockable=True, *args, **kwargs):
    """To launch the ui and not get the same instance

    Returns:
        Anim_picker: instance

    Args:
        edit (bool, optional): Description
        dockable (bool, optional): Description

    """
    return anim_picker_gui.load(edit=edit, dockable=dockable)
