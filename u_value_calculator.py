#Date of start:2023/1/26
#This is the module file for U value calculator
import tkinter as tk
from tkinter import ttk

def choose_u_calculator():
	'''
	'''
	global data_1
	global data_2
	global data_3
	global data_4
	global data_5
	global data_out

	def choose_material(event):

		'''This is the function for choosing material command'''

		list_for_material = ["Asphalt","Bitumen","Ceramic","Clay","Glass",
							"Rubber","Foam","Brick","Cement","Plaster",
							"Concrete blocks","Concrete","Masonry","Stone",
							"Wood","Zinc","Mortar","Timber Frame","Plywood"]
		list_for_λ = ['0.5','0.2','1.4','1.2','1.05','0.17','0.04','0.72',
						'0.72','0.24','0.32','0.19','1.21','0.12','0.55',
						'0.19','0.18','0.88','0.13','0.12']

		choose_1 = box_choose_material1.get()
		choose_2 = box_choose_material2.get()
		choose_3 = box_choose_material3.get()
		choose_4 = box_choose_material4.get()
		choose_5 = box_choose_material5.get()

		if choose_1 in list_for_material:
			material1_index = list_for_material.index(choose_1)
			data_1.set(list_for_λ[material1_index])

		if choose_2 in list_for_material:
			material2_index = list_for_material.index(choose_2)	
			data_2.set(list_for_λ[material2_index])

		if choose_3 in list_for_material:
			material3_index = list_for_material.index(choose_3)	
			data_3.set(list_for_λ[material3_index])

		if choose_4 in list_for_material:
			material4_index = list_for_material.index(choose_4)	
			data_4.set(list_for_λ[material4_index])

		if choose_5 in list_for_material:
			material5_index = list_for_material.index(choose_5)	
			data_5.set(list_for_λ[material5_index])

	def calculate():

		'''This is the function that for calculating command'''

		D1 = float(entry_thickness1.get())
		λ1 = float(entry_λ1.get())
		
		D2 = float(entry_thickness2.get())
		λ2 = float(entry_λ2.get())

		D3 = float(entry_thickness3.get())
		λ3 = float(entry_λ3.get())

		D4 = float(entry_thickness4.get())
		λ4 = float(entry_λ4.get())

		D5 = float(entry_thickness5.get())
		λ5 = float(entry_λ5.get())
	
		R1 = float(D1/λ1)
		R2 = float(D2/λ2)
		R3 = float(D3/λ3)
		R4 = float(D4/λ4)	
		R5 = float(D5/λ5)

		Rt = float(R1+R2+R3+R4+R5)
		num = 1

		U = float(num/Rt)
		result = float(format(U,'.3f'))
		data_out.set(result)
		label_dataout.update()
		print(result)

		return result


	''' Create the window for calculator and some foundation layout design'''

	root = tk.Toplevel()
	root.title("U-value Calculator")
	root.geometry ("750x400")


	label_slogan1 = tk.Label(root,text="U=1/Rt",font="Helvetic 12")
	label_slogan2 = tk.Label(root,text="Rt=R1+R2+R3+....+Rn",font="Helvetic 12")
	label_slogan1.grid(row=0,column=0,padx=50,pady=20)
	label_slogan2.grid(row=0,column=1,padx=25,pady=25)

	label_R = tk.Label(root,text="R",font="Helvetic 12")
	lable_material = tk.Label(root,text="Material",font="Helvetic 12")
	label_thickness = tk.Label(root,text="Thickness(m)",font="Helvetic 12")
	label_λ = tk.Label(root,text="λ(W/K.m)",font="Helvetic 12")
	label_R.grid(row=1,column=0)
	lable_material.grid(row=1,column=1)
	label_thickness.grid(row=1,column=2)
	label_λ.grid(row=1,column=3,padx=25)

	label_R1 = tk.Label(root,text="R1",font="Hevetic 12")
	label_R1.grid(row=2,column=0,pady=10)

	box_choose_material1 = ttk.Combobox(root,width=5)
	box_choose_material1['value'] = ("Asphalt","Bitumen","Ceramic","Clay","Glass",
							"Rubber","Foam","Brick","Cement","Plaster",
							"Concrete blocks","Concrete","Masonry","Stone",
							"Wood","Zinc","Mortar","Timber Frame","Plywood")
	box_choose_material1.bind("<<ComboboxSelected>>",choose_material)
	box_choose_material1.grid(row=2,column=1,ipadx=35)

	entry_thickness1 = tk.Entry(root,width=10)
	entry_thickness1.insert(0,"0")
	entry_thickness1.grid(row=2,column=2)

	data_1=tk.StringVar()
	entry_λ1 = tk.Entry(root,width=10,textvariable=data_1)
	entry_λ1.insert(0,"1")
	entry_λ1.grid(row=2,column=3)


	label_R2 = tk.Label(root,text="R2",font="Hevetic 12")
	label_R2.grid(row=3,column=0,pady=10)

	box_choose_material2 = ttk.Combobox(root,width=5)
	box_choose_material2['value'] = ("Asphalt","Bitumen","Ceramic","Clay","Glass",
							"Rubber","Foam","Brick","Cement","Plaster",
							"Concrete blocks","Concrete","Masonry","Stone",
							"Wood","Zinc","Mortar","Timber Frame","Plywood")
	box_choose_material2.bind("<<ComboboxSelected>>",choose_material)
	box_choose_material2.grid(row=3,column=1,ipadx=35)

	entry_thickness2 = tk.Entry(root,width=10)
	entry_thickness2.insert(0,'0')
	entry_thickness2.grid(row=3,column=2)
	
	data_2=tk.StringVar()
	entry_λ2 = tk.Entry(root,width=10,textvariable=data_2)
	entry_λ2.insert(0,"1")
	entry_λ2.grid(row=3,column=3)

 
	label_R3 = tk.Label(root,text="R3",font="Hevetic 12")
	label_R3.grid(row=4,column=0,pady=10)

	box_choose_material3 = ttk.Combobox(root,width=5)
	box_choose_material3['value'] = ("Asphalt","Bitumen","Ceramic","Clay","Glass",
							"Rubber","Foam","Brick","Cement","Plaster",
							"Concrete blocks","Concrete","Masonry","Stone",
							"Wood","Zinc","Mortar","Timber Frame","Plywood")
	box_choose_material3.bind("<<ComboboxSelected>>",choose_material)
	box_choose_material3.grid(row=4,column=1,ipadx=35)

	entry_thickness3 = tk.Entry(root,width=10)
	entry_thickness3.insert(0,"0")
	entry_thickness3.grid(row=4,column=2)

	data_3 = tk.StringVar()
	entry_λ3 = tk.Entry(root,width=10,textvariable=data_3)
	entry_λ3.insert(0,"1")
	entry_λ3.grid(row=4,column=3)


	label_R4 = tk.Label(root,text="R4",font="Hevetic 12")
	label_R4.grid(row=5,column=0,pady=10)

	box_choose_material4 = ttk.Combobox(root,width=5)
	box_choose_material4['value'] = ("Asphalt","Bitumen","Ceramic","Clay","Glass",
							"Rubber","Foam","Brick","Cement","Plaster",
							"Concrete blocks","Concrete","Masonry","Stone",
							"Wood","Zinc","Mortar","Timber Frame","Plywood")
	box_choose_material4.bind("<<ComboboxSelected>>",choose_material)
	box_choose_material4.grid(row=5,column=1,ipadx=35)

	entry_thickness4 = tk.Entry(root,width=10)
	entry_thickness4.insert(0,"0")
	entry_thickness4.grid(row=5,column=2)

	data_4 = tk.StringVar()
	entry_λ4 = tk.Entry(root,width=10,textvariable=data_4)
	entry_λ4.insert(0,"1")
	entry_λ4.grid(row=5,column=3)


	label_R5 = tk.Label(root,text="R5",font="Hevetic 12")
	label_R5.grid(row=6,column=0,pady=10)

	box_choose_material5 = ttk.Combobox(root,width=5)
	box_choose_material5['value'] = ("Asphalt","Bitumen","Ceramic","Clay","Glass",
							"Rubber","Foam","Brick","Cement","Plaster",
							"Concrete blocks","Concrete","Masonry","Stone",
							"Wood","Zinc","Mortar","Timber Frame","Plywood")
	box_choose_material5.bind("<<ComboboxSelected>>",choose_material)
	box_choose_material5.grid(row=6,column=1,ipadx=35)

	entry_thickness5 = tk.Entry(root,width=10)
	entry_thickness5.insert(0,"0")
	entry_thickness5.grid(row=6,column=2)

	data_5 = tk.StringVar()
	entry_λ5 = tk.Entry(root,width=10,textvariable=data_5)
	entry_λ5.insert(0,"1")
	entry_λ5.grid(row=6,column=3)


	button_cal = tk.Button(root,text="Calculate",font="Hevetic 12",
							command=calculate)
	button_cal.grid(row=7,column=3)

	data_out = tk.StringVar()
	data_out.set("0")
	label_res =tk.Label(root,text="U-value =",font="Helvetic 12")
	label_res.grid(row=8,column=2)
	label_dataout = tk.Label(root,textvariable=data_out,font="Helvetic 12 bold")
	label_dataout.grid(row=8,column=3)
	label_unit =tk.Label(root,text="W/K.m^2",font="Helvetic 12")
	label_unit.grid(row=8,column=4,padx=5)

	root.mainloop()

	


