# Date of the first creation: 2022-12-01
# This file is for EnergyPlus parametric simulation
import json
from StaticEplusEngine import run_eplus_model, convert_json_idf

def run_two_simulation_helper(eplus_run_path, idf_path, this_output_dir,
                                parameter_key_1, parameter_key_2, 
                                parameter_val_1, parameter_val_2):
    """
    This is a helper function to run two simuations with the changed
    values of the parameter_key_1 and parameter_key_2
    """
    ######### step 1: convert an IDF file into JSON file #########
    print(idf_path)
    print(eplus_run_path)
    convert_json_idf(eplus_run_path, idf_path)
    print('convert')
    epjson_path = idf_path.split('.idf')[0] + '.epJSON'
    
    ######### step 2: Load the JSON file into a JSON dict #########
    with open(epjson_path) as  epJSON:
        epjson_dict = json.load(epJSON)
    
    ######### step 3: change the JSON dict value #########
    # ['WindowMaterial:SimpleGlazingSystem', 
    #                            'SimpleWindow:DOUBLE PANE WINDOW',
    #                            'solar_heat_gain_coefficient']
    #['WindowMaterial:SimpleGlazingSystem', 
    #                            'SimpleWindow:DOUBLE PANE WINDOW',
    #                            'u_factor']
    inner_dict = epjson_dict
    for i in range(len(parameter_key_1)):
        if i < len(parameter_key_1) -1:
            inner_dict = inner_dict[parameter_key_1[i]]
    inner_dict[parameter_key_1[-1]] = parameter_val_1
    
    inner_dict = epjson_dict
    for i in range(len(parameter_key_2)):
        if i < len(parameter_key_2) -1:
            inner_dict = inner_dict[parameter_key_2[i]]
    inner_dict[parameter_key_2[-1]] = parameter_val_2

    ######### step 4: dump the JSON dict to JSON file #########
    with open(epjson_path, 'w') as epjson:
        json.dump(epjson_dict, epjson)

    ######### step 5: convert JSON file to IDF file #########
    convert_json_idf(eplus_run_path, epjson_path)


    ######### step 6: run simulation #########
    run_eplus_model(eplus_run_path, idf_path, this_output_dir)

    return this_output_dir + '/eplusout.csv'
