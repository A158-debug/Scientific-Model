import json
from flask_cors import CORS
from flask import Flask, request

from G_Optimization_class import Do_G_Optimization
from Load_structure_info_new import Extract_Structure_Info

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def App():
    return "Welcome to Server"


@app.route("/file_data",methods=['POST'])
def File_Read_Function():
    FileInput = request.get_json()
    FileInputDictonary = json.loads(FileInput['body'])
    # print(FileInputDictonary['fileData'])
    # print(type(FileInputDictonary))
    #--------- File_Input_data = FileInput['body'].split(':')[1].strip("}")-----------
     
    # File_Input_data_with_n = str(FileInput['body'].strip('{"fileData":}'))
    # print(File_Input_data_with_n, file=open('Testfile2.txt', 'w'))
    # File_Input_data_with = File_Input_data_with_n.split('\n')
    # print(File_Input_data_with, file=open('Testfile.txt', 'w'))


    
    class_Extract_Structure_Info = Extract_Structure_Info(FileInputDictonary['fileData'])
    # class_Extract_Structure_Info.print_input_string()
    extracted_info_data = class_Extract_Structure_Info.extract_info()
    # print( extracted_info_data )
    
    # print(FileInput['body'])

    return {'output': {
    "Material_Name": "FeGe",
    "Lattice_Type": "P",
    "Inequivalent_Atoms": "2",
    "Mult_List": ['4', '4'],
    "Atom_Name_List": "['Fe', 'Ge']",
    "Atom_Z_List": "['26.0', '32.0']",
    "Lattice_Parameter": ['0.46999998277320004', '0.46999998277320004', '0.46999998277320004', '90.0', '90.0', '90.0'],
    "X_Coordinate_List": ['0.13500000', '0.63500000', '0.86500000', '0.36500000', '0.84200000', '0.34200000', '0.15800000', '0.65800000'],
    "Y_Coordinate_List": ['0.13500000', '0.36500000', '0.63500000', '0.86500000', '0.84200000', '0.65800000', '0.34200000', '0.15800000'],
    "Z_Coordinate_List": ['0.13500000', '0.86500000', '0.36500000', '0.63500000', '0.84200000', '0.15800000', '0.65800000', '0.34200000']
    }}
    
@app.route("/g_optimized_values",methods=['GET','POST'])
def G_Optimization_output_function():
    G_Optimization_class = Do_G_Optimization()
    Output_G_points_parameter= G_Optimization_class.ON_DO_CALCULATE_G_OPTIMIZATION()  
    # print(Output_G_points_parameter)
    return {"Output_G_points_parameter": Output_G_points_parameter} 
    # Output format {h, k, l, Vg(Volt), Phase, Extinction_distance}

if __name__ == '__main__':
    app.run(host='0.0.0.0')