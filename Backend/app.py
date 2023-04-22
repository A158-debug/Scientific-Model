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
    FileInput = request.get_json()   # parse the incomming json request
    FileInputDictonary = json.loads(FileInput['body'])
    
    global extracted_info_data
    class_Extract_Structure_Info = Extract_Structure_Info(FileInputDictonary['fileData'])
    extracted_info_data = class_Extract_Structure_Info.Extract_Info()

    return extracted_info_data

    
@app.route("/g_optimized_values",methods=['GET','POST'])
def G_Optimization_output_function():
    Magentic_Atoms_response = request.get_json() 
    Magnetic_Atoms = json.loads(Magentic_Atoms_response['magnetic_atom_dict'])
    
    extracted_data_with_magnetic_atoms = {};
    extracted_data_with_magnetic_atoms['magnetic_atoms'] = Magnetic_Atoms['magneticAtoms']
    extracted_data_with_magnetic_atoms['extracted_data'] = extracted_info_data['output']

    G_Optimization_class = Do_G_Optimization(extracted_data_with_magnetic_atoms)
    Output_G_points_parameter, Output_Optimized_G_Parameters= G_Optimization_class.ON_DO_CALCULATE_G_OPTIMIZATION()
    
    return {"Output_G_points_parameter": Output_G_points_parameter,"Output_Optimized_G_Parameters":Output_Optimized_G_Parameters} 
  

if __name__ == '__main__':
    app.run(host='0.0.0.0')