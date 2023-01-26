from flask import Flask, request
from flask_cors import CORS
import json
from  G_Optimization_class2 import All_G_points_parameter
# print(len(All_G_points_parameter))
app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def Hello():
    print(len(All_G_points_parameter))
    return {'output':All_G_points_parameter}
    return "Welcome to ElectronNova Server"


@app.route("/file-data",methods=['POST'])
def pie_equipment():
    FileData = request.get_json()
    return {'output': {
    "Material_Name": "FeGe",
    "Lattice_Type": "P",
    "Inequivalent_Atoms": "2",
    "Mult_List": ['4', '4'],
    "Atom_Name_List": "['Fe', 'Ge']",
    "Atom_Z_List": "['26.0', '32.0']",
    "Lattice_Parameter": [0.46999998277320004, 0.46999998277320004, 0.46999998277320004, 90.0, 90.0, 90.0],
    "X_Coordinate_List": ['0.13500000', '0.63500000', '0.86500000', '0.36500000', '0.84200000', '0.34200000', '0.15800000', '0.65800000'],
    "Y_Coordinate_List": ['0.13500000', '0.36500000', '0.63500000', '0.86500000', '0.84200000', '0.65800000', '0.34200000', '0.15800000'],
    "Z_Coordinate_List": ['0.13500000', '0.86500000', '0.36500000', '0.63500000', '0.84200000', '0.15800000', '0.65800000', '0.34200000']
    }}

if __name__ == '__main__':
    app.run(host='0.0.0.0')