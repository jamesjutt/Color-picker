"""
Program: colorpicker.py
Author: James Jutt
Date: 3/28/19

Program allows the user to select a color from the OS color package.
The GUI-based interface will display that color's RGB values and Hex color values.
"""

from breezypythongui import EasyFrame
import tkinter.colorchooser

class ColorPicker(EasyFrame):
    """Displays the result of picking a color"""
    def __init__(self):
        """Sets up the window and the widgets"""
        EasyFrame.__init__(self, title = "Color Chooser Demo")

        #Labels and output fields
        self.addLabel(text = "R", row = 0, column = 0)
        self.r = self.addIntegerField(value = 0, row = 0, column = 1)
    
        self.addLabel(text = "G", row = 1, column = 0)
        self.g = self.addIntegerField(value = 0, row = 1, column = 1)

        self.addLabel(text = "B", row = 2, column = 0)
        self.b = self.addIntegerField(value = 0, row = 2, column = 1)

        self.addLabel(text = "Color", row = 3, column = 0)
        self.hex = self.addTextField(text = "", row = 3, column = 1, width = 10)

        # Canvas with an initial black background
        self.canvas = self.addCanvas(row = 0, column = 2, rowspan = 4, width = 50, background = "#000000")

        # Command button
        self.addButton(text = "Choose color", row = 4, column = 0, columnspan = 3, command = self.chooseColor)

    def chooseColor(self):
        """Pops up a color chooser and outputs the results."""
        colorTuple = tkinter.colorchooser.askcolor()
        if not colorTuple[0]:
            return
        ((r, g, b), hexString) = colorTuple
        self.r.setNumber(int(r))
        self.g.setNumber(int(g))
        self.b.setNumber(int(b))
        self.hex.setText(hexString)
        self.canvas["background"] = hexString
        

def main():
    ColorPicker().mainloop()
if __name__ == "__main__":
    main()