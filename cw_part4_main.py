#Date of the first creation: 2023-01-17
#This file is for Practical tools for Engineering
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from u_value_calculator import *
from unit_converter import *


def specification_u_calculator():

	'''This is the function that contains the specification 
		for U-value calculator'''

	root2 = tk.Toplevel()
	root2.title("The specification of u-value calcuator")
	root2.geometry("700x400")
	label_spec_cal = tk.Label(root2,text="This is the specification of u-value"
											"calculator,please follow the"
											"following steps to use the calculator:"
								,font="Helvetic 12",wraplength=500,anchor="nw")
	label_spec_cal_1 = tk.Label(root2,text="1.Click the Calculator button to open "
											"the calculator"
								,font="Helvetic 12",wraplength=500,anchor="nw")
	label_spec_cal_2 = tk.Label(root2,text="2.Select each layer of material in the "
											"first combobox. the default λ value "
											"will display in the third combobox"
								,font="Helvetic 12",wraplength=550,anchor="nw")
	label_spec_cal_3 = tk.Label(root2,text="3.If the actual λ value of the "
											"material is inconsistent with the "
											"default, you can modify in the third "
											"combobox"
								,font="Helvetic 12",wraplength=550,anchor="nw")
	label_spec_cal_4 = tk.Label(root2,text="4.After material seletion, input the "
											"thickness, note that the unit is m! "
											"then, click the bottom right calculate "
											"button,you can get the answer"
								,font="Helvetic 12",wraplength=550,anchor="nw")
	label_spec_cal_5 = tk.Label(root2,text="4.Note that this calcuator can only "
											"calculate the U value published in "
											"U = 1/Rt, if area or perimeter ratios "
											"are involved, this calcuator cannot do "
											"it"
								,font="Helvetic 12",wraplength=550,anchor="nw")

	label_spec_cal.grid(row=0,column=0,padx=5,pady=5,sticky='nw')
	label_spec_cal_1.grid(row=1,column=0,padx=5,pady=5,sticky='nw')
	label_spec_cal_2.grid(row=2,column=0,padx=5,pady=5,sticky='nw')
	label_spec_cal_3.grid(row=3,column=0,padx=5,pady=5,sticky='nw')
	label_spec_cal_4.grid(row=4,column=0,padx=5,pady=5,sticky='nw')
	label_spec_cal_5.grid(row=5,column=0,padx=5,pady=5,sticky='nw')

def specification_unit_converter():

	'''	This is the function that contains the specification 
		for unit converter'''

	root3 = tk.Toplevel()
	root3.title("The specification of unit converter")
	root3.geometry("700x400")
	label_spec_unit = tk.Label(root3,text="This is the specification of the engineering" 
											"unit converter,please follow the"
											"following steps to use the converter:"
								,font="Helvetic 12",wraplength=500,anchor="nw")
	label_spec_unit_1 = tk.Label(root3,text="1.Click the Converter button to open "
											"the converter"
								,font="Helvetic 12",wraplength=550,anchor="nw")
	label_spec_unit_2 = tk.Label(root3,text="2.In the first combobox,select the" 
											"type of units you want to convert"
								,font="Helvetic 12",wraplength=550,anchor="nw")
	label_spec_unit_3 = tk.Label(root3,text="3.Enter the data to be converted"
								,font="Helvetic 12",wraplength=500,anchor="nw")
	label_spec_unit_4 = tk.Label(root3,text="4.Select the original unit of the"
											" data in the second combo box"
								,font="Helvetic 12",wraplength=500,anchor="nw")
	label_spec_unit_5 = tk.Label(root3,text="5.In the third combo box, select"
											"the unit you want to convert to"
								,font="Helvetic 12",wraplength=550,anchor="nw")
	label_spec_unit.grid(row=0,column=0,padx=5,pady=5,sticky='nw')
	label_spec_unit_1.grid(row=1,column=0,padx=5,pady=5,sticky='nw')
	label_spec_unit_2.grid(row=2,column=0,padx=5,pady=5,sticky='nw')
	label_spec_unit_3.grid(row=3,column=0,padx=5,pady=5,sticky='nw')
	label_spec_unit_4.grid(row=4,column=0,padx=5,pady=5,sticky='nw')
	label_spec_unit_5.grid(row=5,column=0,padx=5,pady=5,sticky='nw')

	

'''Create Windows, and basic settings'''	
root = tk.Tk()
root.title("Practical tools for Engineering")
root.geometry('700x400')

button1 = tk.Button(root,text="U-value Calculator",font="Helvetic 14",
					command=choose_u_calculator)
button2= tk.Button(root,text="Unit converter",font="Helvetic 14",
					command=choose_unit_converter)
button1.grid(row=1,column=0,padx=270,pady=100)
button2.grid(row=2,column=0,padx=270)

menubar = tk.Menu(root)
specification = tk.Menu(menubar,tearoff=1)
menubar.add_cascade(label="Specification",font="Helvetic 12",
						menu=specification)
specification.add_command(label="U-value Calculator",font="Helvetic 12",
							command=specification_u_calculator)
specification.add_command(label="Units converter",font="Helvetic 12",
							command=specification_unit_converter)
specification.add_command(label="Exit!",font="Helvetic 12",
							command=root.destroy)
root.config(menu=menubar)

root.mainloop()