from cw_part3_simulation_helper import Two_simulation

#eplus_run_path, idf_path, this_output_dir,
                             #   parameter_key_1, parameter_key_2, 
                             #   parameter_val_1, parameter_val_2)
eplus_run_path='./energyplus9.5/energyplus'
idf_path='./1ZoneUncontrolled_win_1.idf'
key_1_path = ['WindowMaterial:SimpleGlazingSystem', 'SimpleWindow:DOUBLE PANE WINDOW', 'solar_heat_gain_coefficient'] 
key_2_path = ['WindowMaterial:SimpleGlazingSystem', 'SimpleWindow:DOUBLE PANE WINDOW', 'u_factor']
out_put_dir='./cw_part3_simulation_results' 
key_1_min=0.25
key_1_max=0.5
key_2_min=0.5
key_2_max=0.7
key_1_interval=0.05
key_2_interval=0.025

key_1_values=[]
key_2_values=[]

for i in range(int((key_1_max-key_1_min)/key_1_interval)):
	key_1_values.append(key_1_min+i*key_1_interval)
for i in range(int((key_2_max-key_2_min)/key_2_interval)):
	key_2_values.append(key_2_min+i*key_2_interval)

#	def __init__(self, val_1, val_2,out_put_dir,key_1,key_2,idf_path,eplus_run_path):



sim= Two_simulation(key_1_values,key_2_values,out_put_dir,key_1_path,key_2_path,idf_path,eplus_run_path)
sim.parameter_combination()
sim.run_simulation()
r=sim.run_result()
print('highest average value: '+r.split(':')[1]+' Key 1 value: '+r.split(':')[0].split('_')[0]+' Key 2 value: '+r.split(':')[0].split('_')[1])
#sim().run_two_simulation_helper(eplus_run_path,idf_path,out_put_dir,key_1_path,key_1_values,key_2_path,key_2_values)

