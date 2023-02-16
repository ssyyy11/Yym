# Date of the first creation: 2022-12-02
# This file is for two parameters simulation, there is a class 
# to do this work. the class can take any two arbitrary simulation
# model parameters and their ranges, and return the best set of 
# parameter values with which the simulation has the 
# highest average indoor air temperature.
from cw_part3_parameter_helper import run_two_simulation_helper

import pandas as pd

#Usage:
# init 
# combine data
#run two simulation
# get result
class Two_simulation:
	'''a class for two parameters simulation'''

	def __init__(self, val_1, val_2,out_put_dir,key_1,key_2,idf_path,eplus_run_path):
		'''initializes the description parameter properties '''
		self.val_1 = val_1
		self.val_2 = val_2
		self.out_put_dir=out_put_dir
		self.key_1=key_1 
		self.key_2=key_2
		self.idf_path=idf_path
		self.eplus_run_path=eplus_run_path
		self.result_dir={}
		self.average_dir={}


	def parameter_combination(self):
		'''pairs the parameters '''
		L_1 = self.val_1
		L_2 = self.val_2

		self.L_3 = [[a,b] for a in L_1 for b in L_2]#list or tuples?

	def run_simulation(self):
		if len(self.L_3)==0:
			print("Please Init data first")
			return

		for l in self.L_3:
			self.result_dir[str(l[0])+'_'+str(l[1])]=run_two_simulation_helper(self.eplus_run_path,self.idf_path,self.out_put_dir+'/'+str(l[0])+'_'+str(l[1]),self.key_1,self.key_2,l[0],l[1])
		print('done with, ')
		print(self.result_dir)
	def run_result(self):
	  highest_value=None
	  k_1=None
	  k_2=None
	  for key in self.result_dir.keys():
	    tb=pd.read_csv(self.result_dir[key])
	    data=tb['ZONE ONE:Zone Mean Air Temperature [C](TimeStep) ']
	    average=sum(data)/len(data)
	    if highest_value is None or highest_value<average:
	      highest_value=average
	      k_1=key.split('_')[0]
	      k_2=key.split('_')[1]
	    self.average_dir[key]=highest_value
	  print(self.average_dir)
	  return str(k_1)+'_'+str(k_2)+':'+str(highest_value)




