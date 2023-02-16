#Date of the first creation: 2023-01-17
#This is a module file is for  unit converter
import tkinter as tk
from tkinter import ttk

def choose_unit_converter():
	
	global data
	global data_out

	def choose_unit_class(event):

		''' This is the function that for class choose combobox.
			it helps the unit1 and unit2 comboboxs change with the
			different unit classes.'''


		choose = box_choose_unit_class.get()
		list_1 = []
		print(choose)
		if choose == "Volume":
			list_1 = ['please choose the unit1','mm^3','mL(cm^3)','L(dm^3)',
						'm^3','km^3']
			list_2 = ['please choose the unit2','mm^3','mL(cm^3)','L(dm^3)','m^3','km^3']
		elif choose == "Length":
			list_1 = ['please choose the unit1','mm','cm','dm','m','km']
			list_2 = ['please choose the unit2','mm','cm','dm','m','km']
		elif choose == 'Area':
			list_1 = ['please choose the unit1','mm^2','cm^2','dm^2','m^2','hm^2']
			list_2 = ['please choose the unit2','mm^2','cm^2','dm^2','m^2','hm^2']
		elif choose == "Temperature":
			list_1 = ['please choose the unit1',' degree Kelvin','degree centigrade','degree Fahrenheit']
			list_2 = ['please choose the unit2',' degree Kelvin','degree centigrade','degree Fahrenheit']
		elif choose == 'Pressure':
			list_1 = ['please choose the unit1','MPa','atm','kPa','hPa','daPa','Pa','dPa','cPa','mPa','miuPa',
						'nPa','pPa','fPa']
			list_2 = ['please choose the unit2','MPa','atm','kPa','hPa','daPa','Pa','dPa','cPa','mPa','miuPa',
						'nPa','pPa','fPa']
		elif choose == 'Energy':
			list_1 = ['please choose the unit1','MJ','kJ','J','mJ','miuJ','nJ']
			list_2 = ['please choose the unit2','MJ','kJ','J','mJ','miuJ','nJ']
		elif choose == 'Power':
			list_1 = ['please choose the unit1','kW','hW','daW','W','dW','mW','miuW','nW','pW']
			list_2 = ['please choose the unit2','kW','hW','daW','W','dW','mW','miuW','nW','pW']
		elif choose == 'Force':
			list_1 = ['please choose the unit1','kN','N','dN','kN','cN','mN','miuN','nN','pN','fN']
			list_2 = ['please choose the unit2','kN','N','dN','kN','cN','mN','miuN','nN','pN','fN']
		elif choose == 'Velocity':
			list_1 = ['please choose the unit1','m/s','km/h','m/h','m/min','km/min','km/s']
			list_2 = ['please choose the unit2','m/s','km/h','m/h','m/min','km/min','km/s']
		elif choose == 'Density':
			list_1 = ['please choose the unit1','kg/cm^2','g/mm^2','g/cm^2','mg/mm^2','kg/m^2','mg/cm^2','g/m^2',
						'mg/m^2']
			list_2 = ['please choose the unit2','kg/cm^2','g/mm^2','g/cm^2','mg/mm^2','kg/m^2','mg/cm^2','g/m^2',
						'mg/m^2']
		elif choose == 'Mass concentration':
			list_1 = ['please choose the unit1','kg/L','g/L','mg/L']
			list_2 = ['please choose the unit2','kg/L','g/L','mg/L']
		elif choose == 'Molarity':
			list_1 = ['please choose the unit1','mol/cm^3','mol/L','mol/m^3']
			list_2 = ['please choose the unit2','mol/cm^3','mol/L','mol/m^3']
		elif choose == 'Surface tension':
			list_1 = ['please choose the unit1','N/m','mN/m','dyne/cm','gf/cm']
			list_2 = ['please choose the unit2','N/m','mN/m','dyne/cm','gf/cm']
		elif choose == 'Viscosity':
			list_1 = ['please choose the unit1','m^2/s','m^2/h','cm^2/s','mm^2/s']
			list_2 = ['please choose the unit2','m^2/s','m^2/h','cm^2/s','mm^2/s']
		box_choose_unit1['value'] = list_1
		box_choose_unit2['value'] = list_2

	def convert(event):

		''' After selecting the unit category, the specific unit is
			further determined, then doing the conversion'''


		unit_class = box_choose_unit_class.get()
		if unit_class == "Volume":
			data_out.set(convert_V(data,box_choose_unit1.get(),box_choose_unit2.get()))
		if unit_class == "Length":
			data_out.set(convert_L(data,box_choose_unit1.get(),box_choose_unit2.get()))
		if unit_class == "Area":
			data_out.set(convert_S(data,box_choose_unit1.get(),box_choose_unit2.get()))
		if unit_class == "Temperature":
			data_out.set(convert_T(data,box_choose_unit1.get(),box_choose_unit2.get()))
		if unit_class == "Pressure":
			data_out.set(convert_p(data,box_choose_unit1.get(),box_choose_unit2.get()))
		if unit_class == "Energy":
			data_out.set(convert_E(data,box_choose_unit1.get(),box_choose_unit2.get()))
		if unit_class == "Power":
			data_out.set(convert_P(data,box_choose_unit1.get(),box_choose_unit2.get()))
		if unit_class == "Force":
			data_out.set(convert_F(data,box_choose_unit1.get(),box_choose_unit2.get()))
		if unit_class == "Velocity":
			data_out.set(convert_v(data,box_choose_unit1.get(),box_choose_unit2.get()))
		if unit_class == "Density":
			data_out.set(convert_ρ(data,box_choose_unit1.get(),box_choose_unit2.get()))
		if unit_class == "Mass concentration":
			data_out.set(convert_ρ_for_m(data,box_choose_unit1.get(),box_choose_unit2.get()))
		if unit_class == "Molarity":
			data_out.set(convert_M(data,box_choose_unit1.get(),box_choose_unit2.get()))
		if unit_class == "Surface tension":
			data_out.set(convert_σ(data,box_choose_unit1.get(),box_choose_unit2.get()))
		if unit_class == "Viscosity":
			data_out.set(convert_μ(data,box_choose_unit1.get(),box_choose_unit2.get()))
		label_output_result.update()


	def convert_V(n,unit1,unit2):

		'''Volumetric unit conversion'''

		c = [1000000000,1000000,1000,1,0.000000001]
		l = ['mm^3','mL(cm^3)','L(dm^3)','m^3','km^3']
		if unit1 not in l or unit2 not in l:
			result = 0
		else:
			unit1_index = l.index(unit1)
			unit2_index = l.index(unit2)
			print(type(n))
			print(n.get())
			num=float(n.get())
			result = float(num/c[unit1_index]*c[unit2_index])
		return result


	def convert_L(n,unit1,unit2):

		'''Length unit conversion'''

		c = [1000,100,10,1,0.001]
		l = ['mm','cm','dm','m','km']
		if unit1 not in l or unit2 not in l:
			result = 0
		else:
			unit1_index = l.index(unit1)
			unit2_index = l.index(unit2)
			print(type(n))
			print(n.get())
			num=float(n.get())
			result = float(num/c[unit1_index]*c[unit2_index])
		return result

	def convert_S(n,unit1,unit2):

		'''Area unit conversion'''

		c = [1000000,10000,100,1,0.0001]
		l = ['mm^2','cm^2','dm^2','m^2','hm^2']
		if unit1 not in l or unit2 not in l:
			result = 0
		else:
			unit1_index = l.index(unit1)
			unit2_index = l.index(unit2)
			print(type(n))
			print(n.get())
			num = float(n.get())
			result = float(num/c[unit1_index]*c[unit2_index])
		return result

	def convert_T(n,unit1,unit2):

		'''Temperature unit conversion'''

		l = [' degree Kelvin','degree centigrade','degree Fahrenheit']
		if unit1 not in l or unit2 not in l:
			result = 0
		if unit1 == unit2:
			print(type(n))
			print(n.get())
			result = float(n.get()) 
		if unit1 == l[0] and unit2 ==l[1] or unit2 == l[0] and unit1 == l[1]:
			print(type(n))
			print(n.get())
			num = float(n.get())
			result = float(num-273.15)
		if unit1 == l[1] and unit2 == l[2]:
			unit1_index = l.index(unit1)
			unit2_index = l.index(unit2)
			print(type(n))
			print(n.get())
			num = float(n.get())
			result = float(num*1.8+32)
		if unit1 == l[2] and unit2 == l[1]:
			unit1_index = l.index(unit1)
			unit2_index = l.index(unit2)
			print(type(n))
			print(n.get())
			num = float(n.get())
			result = float((num-32)/1.8)
		if unit1 == l[0] and unit2 == l[2]:
			unit1_index = l.index(unit1)
			unit2_index = l.index(unit2)
			print(type(n))
			print(n.get())
			num = float(n.get())
			result = float((num-272.15)*1.8+32)
		if unit1 == l[2] and unit2 == l[0]:
			unit1_index = l.index(unit1)
			unit2_index = l.index(unit2)
			print(type(n))
			print(n.get())
			num = float(n.get())
			result = float((num-32)/1.8+272.15)
		return result

	def convert_p(n,unit1,unit2):

		'''Pressure unit converison'''

		c = [0.000001,0.00000098692,0.001,0.01,0.1,1,10,100,1000,
				1000000,1000000000,1000000000000,1000000000000000]
		l = ['MPa','atm','kPa','hPa','daPa','Pa','dPa','cPa','mPa','miuPa',
				'nPa','pPa','fPa']
		if unit1 not in l or unit2 not in l:
			result = 0
		else:
			unit1_index = l.index(unit1)
			unit2_index = l.index(unit2)
			print(type(n))
			print(n.get())
			num = float(n.get())
			result = float(num/c[unit1_index]*c[unit2_index])
		return result

	def convert_E(n,unit1,unit2):

		'''Energy unit converison'''

		c = [0.000001,0.001,1,1000,1000000,1000000000]
		l = ['MJ','kJ','J','mJ','miuJ','nJ']
		if unit1 not in l or unit2 not in l:
			result = 0
		else:
			unit1_index = l.index(unit1)
			unit2_index = l.index(unit2)
			print(type(n))
			print(n.get())
			num = float(n.get())
			result = float(num/c[unit1_index]*c[unit2_index])
		return result

	def convert_P(n,unit1,unit2):

		'''Power unit converison'''

		c = [0.001,0.01,0.1,1,10,1000,1000000,1000000000,1000000000000]
		l = ['kW','hW','daW','W','dW','mW','miuW','nW','pW']
		if unit1 not in l or unit2 not in l:
			result = 0
		else:
			unit1_index = l.index(unit1)
			unit2_index = l.index(unit2)
			print(type(n))
			print(n.get())
			num = float(n.get())
			result = float(num/c[unit1_index]*c[unit2_index])
		return result

	def convert_F(n,unit1,unit2):

		'''Force unit conversion'''

		c = [0.001,1,10,100,1000,1000000,1000000000,10000000000000,
				1000000000000000]
		l = ['kN','N','dN','kN','cN','mN','miuN','nN','pN','fN']
		if unit1 not in l or unit2 not in l:
			result = 0
		else:
			unit1_index = l.index(unit1)
			unit2_index = l.index(unit2)
			print(type(n))
			print(n.get())
			num = float(n.get())
			result = float(num/c[unit1_index]*c[unit2_index])
		return result

	def convert_v(n,unit1,unit2):

		''' Velocity unit conversion'''

		c = [1,3.6,3600,60,0.06,0.001]
		l = ['m/s','km/h','m/h','m/min','km/min','km/s']
		if unit1 not in l or unit2 not in l:
			result = 0
		else:
			unit1_index = l.index(unit1)
			unit2_index = l.index(unit2)
			print(type(n))
			print(n.get())
			num = float(n.get())
			result = float(num/c[unit1_index]*c[unit2_index])
		return result

	def convert_ρ(n,unit1,unit2):

		'''  Density unit conversion'''

		c = [0.000001,0.000001,0.001,0.001,1,1,1000,1000000]
		l = ['kg/cm^2','g/mm^2','g/cm^2','mg/mm^2','kg/m^2','mg/cm^2','g/m^2',
				'mg/m^2']
		if unit1 not in l or unit2 not in l:
			result = 0
		else:
			unit1_index = l.index(unit1)
			unit2_index = l.index(unit2)
			print(type(n))
			print(n.get())
			num = float(n.get())
			result = float(num/c[unit1_index]*c[unit2_index])
		return result

	def convert_ρ_for_m (n,unit1,unit2):

		''' Mass concentration unit conversion'''

		c = [1,1000,1000000]
		l = ['kg/L','g/L','mg/L']
		if unit1 not in l or unit2 not in l:
			result = 0
		else:
			unit1_index = l.index(unit1)
			unit2_index = l.index(unit2)
			print(type(n))
			print(n.get())
			num = float(n.get())
			result = float(num/c[unit1_index]*c[unit2_index])
		return result

	def convert_M (n,unit1,unit2):

		''' Molarity unit conversion'''

		c = [0.000001,0.001,1]
		l = ['mol/cm^3','mol/L','mol/m^3']
		if unit1 not in l or unit2 not in l:
			result = 0
		else:
			unit1_index = l.index(unit1)
			unit2_index = l.index(unit2)
			print(type(n))
			print(n.get())
			num = float(n.get())
			result = float(num/c[unit1_index]*c[unit2_index])
		return result

	def convert_σ (n,unit1,unit2):

		''' Surface tesnison unit conversion'''

		c = [1,1000,1000,1.019716213]
		l = ['N/m','mN/m','dyne/cm','gf/cm']
		if unit1 not in l or unit2 not in l:
			result = 0
		else:
			unit1_index = l.index(unit1)
			unit2_index = l.index(unit2)
			print(type(n))
			print(n.get())
			num = float(n.get())
			result = float(num/c[unit1_index]*c[unit2_index])
		return result

	def convert_μ (n,unit1,unit2):

		''' Viscosity unit conversion'''

		c = [1,3600,10000,1000000]
		l = ['m^2/s','m^2/h','cm^2/s','mm^2/s']
		if unit1 not in l or unit2 not in l:
			result = 0
		else:
			unit1_index = l.index(unit1)
			unit2_index = l.index(unit2)
			print(type(n))
			print(n.get())
			num = float(n.get())
			result = float(num/c[unit1_index]*c[unit2_index])
		return result


	'''Create the Window for converter and some foundation layout design'''
	root = tk.Toplevel()
	root.title("Engineering unit converter")
	root.geometry('500x300')

	label_slogan = tk.Label(root, text='Select the unit class you want to convert'
							,font="Helvetic 12")
	label_slogan.grid(row=0,column=0,sticky='nw')

	box_choose_unit_class = ttk.Combobox(root)
	box_choose_unit_class['value'] = ('Volume','Length','Area','Temperature',
										'Pressure','Energy','Power','Force',
										'Velocity','Density','Mass concentration',
										'Molarity','Surface tension','Viscosity')
	box_choose_unit_class.current(0)
	box_choose_unit_class.bind("<<ComboboxSelected>>", choose_unit_class)
	box_choose_unit_class.grid(row=1,column=0,sticky='nw',ipadx=35)

	label_Input = tk.Label(root, text='Input',justify='left',font="Helvetic 12")
	label_Input.grid(row=2,column=0,sticky='nw')

	data = tk.StringVar()
	entry_Input_value = tk.Entry(root, textvariable=data)
	entry_Input_value.insert(6,'Please enter the value here')
	entry_Input_value.bind('<Return>',convert)
	entry_Input_value.grid(row=3,column=0,sticky='nw',ipadx=35)

	box_choose_unit1 = ttk.Combobox(root)
	box_choose_unit1.bind("<<ComboboxSelected>>",convert)
	box_choose_unit1.grid(row=4,column=0,sticky='nw',ipadx=35)

	label_Equal = tk.Label(root, text='Equal',font="Helvetic 12")
	label_Equal.grid(row=5,column=0,sticky='nw')

	data_out = tk.StringVar()
	data_out.set('0')
	label_output_result = tk.Label(root,textvariable=data_out,font="Helvetic 12")
	label_output_result.grid(row=6,column=0,sticky='nw')

	box_choose_unit2 = ttk.Combobox(root)
	box_choose_unit2.bind("<<ComboboxSelected>>",convert)
	box_choose_unit2.grid(row=7,column=0,sticky='nw',ipadx=35)

	root.mainloop()
