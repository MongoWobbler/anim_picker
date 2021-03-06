Copyright (c) 2018 Guillaume Barlier
This file is part of "anim_picker" and covered by MIT,
read LICENSE.md and COPYING.md for details.
https://github.com/gbarlier

## DESCRIPTIONS
The Animation picker tool called "anim_picker" for short is a tool for Maya.
This tool allows you to create a graphical interface for quick animation controls selection.

## DEPENDENCIES
This tool requires PySide2 and Maya.

# Create a new picker
To create a new picker for a animation character start by importing the picker package and loading the interface in edit mode: 

	import anim_picker
	anim_picker.load(edit=True)

Then create a new node by pressing the "new" button, and choose a name for the node (i leave the default name)
To add or modify any picker item simply access the options by right clicking on an empty space on the interface.
You can add/remove/rename tabs by right clicking the tab area.
You can change the character snapshot by right clicking it.
As you can see most interaction are by right clicking the elements and/or empty space and that will open different context menus.

Simply save the picker data node with the character rig as the picker tool will use it's future namespace and data on normal "animation mode"

# Use an existing picker
If a character has an existing picker node, run the following python commands: 

	import anim_picker
	anim_picker.load()
	
That should load the picker node, you have a character selector at the top to navigate between pickers if you have several character in the scene.
Some controls have custom right click context menus too, if specified in the picker or custom click action.
By default the click action should select any associated controls relative to the clicked picker item.
