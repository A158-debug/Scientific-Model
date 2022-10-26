from flask import Flask, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def Hello():
    return "Welcome to ElectronNova Server"


@app.route("/file-data",methods=["GET","POST"])
def pie_equipment():
    FileData = request.get_json()
    print(FileData['filedata'])
    # print(type(FileData['filedata']))
    # with open('readme.struct', 'w') as f:
    #     f.write(FileData['filedata'])
    

    return {'output': [1,2,3]}

if __name__ == '__main__':
    app.run(host='0.0.0.0')