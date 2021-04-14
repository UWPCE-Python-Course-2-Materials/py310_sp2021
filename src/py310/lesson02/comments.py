# --------------------------------------------------------------------------------- #
# AQUABUTTON wxPython IMPLEMENTATION
#
# Andrea Gavana, @ 07 October 2008
# Latest Revision: 24 Nov 2011, 22.00 GMT
#
#
# TODO List
#
# 1) Anything to do?
#
#
# For all kind of problems, requests of enhancements and bug reports, please
# write to me at:
#
# andrea.gavana@gmail.com
# andrea.gavana@maerskoil.com
#
# Or, obviously, to the wxPython mailing list!!!
#
#
# End Of Comments
# --------------------------------------------------------------------------------- #

"""
:class:`AquaButton` is another custom-drawn button class which *approximatively* mimics
the behaviour of Aqua buttons on the Mac.


Description
===========

:class:`AquaButton` is another custom-drawn button class which *approximatively* mimics
the behaviour of Aqua buttons on the Mac. At the moment this class supports:

* Bubble and shadow effects;
* Customizable background, foreground and hover colours;
* Rounded-corners buttons;
* Text-only or image+text buttons;
* Pulse effect on gaining focus.

And a lot more. Check the demo for an almost complete review of the functionalities.


Usage
=====

Sample usage::

    import wx
    import wx.lib.agw.aquabutton as AB

    app = wx.App(0)

    frame = wx.Frame(None, -1, "AquaButton Test")

    mainPanel = wx.Panel(frame)
    mainPanel.SetBackgroundColour(wx.WHITE)

    # Initialize AquaButton 1 (with image)
    bitmap = wx.Bitmap("my_button_bitmap.png", wx.BITMAP_TYPE_PNG)
    btn1 = AB.AquaButton(mainPanel, -1, bitmap, "AquaButton")

    # Initialize AquaButton 2 (no image)
    btn2 = AB.AquaButton(mainPanel, -1, None, "Hello World!")

    frame.Show()

    app.MainLoop()


Supported Platforms
===================

AquaButton has been tested on the following platforms:
  * Windows (Windows XP);
  * Linux Ubuntu (10.10).


Window Styles
=============

`No particular window styles are available for this class.`


Events Processing
=================

This class processes the following events:

================= ==================================================
Event Name        Description
================= ==================================================
``wx.EVT_BUTTON`` Process a `wxEVT_COMMAND_BUTTON_CLICKED` event, when the button is clicked.
================= ==================================================


License And Version
===================

:class:`AquaButton` control is distributed under the wxPython license.

Latest Revision: Andrea Gavana @ 22 Nov 2011, 22.00 GMT

Version 0.4

"""

x = x + 1  # allow for border

BORDER = 1
x = x + BORDER


def allow_for_border(coordinate):
    return coordinate + 1


y = allow_for_border(y)


def calc(num1, num2):
    # calc product 2 numbers
    return num1 + num2


def calculate_product(left, right):
    return left * right
