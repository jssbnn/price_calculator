"""
Program: GUItemplate.py
Author: Jessica 6/15/2022

Final Project WA170 - Python
A GUI- based app that calculates the the cost of inputed quantity of items.
"""

from breezypythongui import EasyFrame
from tkinter import *
import tkinter.font

class CostCalculatorGUI(EasyFrame):
	# definiton of the __init__() method which is our class constructor
	def __init__(self):
		# sets up window and widgets
		EasyFrame.__init__(self, title = "Cost Calculator", width = 350, height = 450, resizable = False, background="darkseagreen")

		# sets up fonts
		titlefont = tkinter.font.Font(family = "Impact", size = 26)
		labelFont = tkinter.font.Font(family = "Helvetica")

		# Title label
		self.addLabel(text="Cost Calculator", row = 0, column = 0, columnspan = 2, sticky = "NEW", background ="darkslategray", foreground = "white", font = titlefont)
		
		# Item cost label and input
		self.addLabel(text="Cost", row = 1, column = 0, background = "darkslategray",  foreground = "white", font = labelFont)
		self.costField = self.addFloatField(value = 0.0, row = 1, column = 0, width = 10, precision = 2, )

		# Item quantity label and input
		self.addLabel(text="Quantity", row = 2, column = 0, background = "darkslategray",foreground = "white", font = labelFont)
		self.quantityField = self.addIntegerField(value = 0, row = 2, column = 0, width = 10)
		
		# the command button
		self.addButton(text = "Calculate", row = 3, column = 0, columnspan = 2, command = self.calculateCost)

		# display final outcome label and output
		self.addLabel(text = "Your total cost is :", row = 4, column = 0, background = "darkslategray", foreground = "white", font = labelFont)
		self.priceOutput = self.addFloatField(value = 0.0, row = 4, column = 0, precision = 2, state = "readonly")

	# Event handling method for the calculate button
	def calculateCost(self):
		# obtain and validate inputs
		price = self.costField.getNumber()
		quantity = self.quantityField.getNumber()

		# calculate and store product
		totalCost = price * quantity
		self.priceOutput.setNumber(totalCost)

# definition of the main method which will establish class objects
def main():
	# instantiate an object from the class into mainloop()
	CostCalculatorGUI().mainloop()

#global call to the main() method
main()