#!flask/bin/python
from flask import Flask, jsonify
import base64

app = Flask(__name__)

with open("corgo.jpg", "rb") as f:
    encodedZip = base64.b64encode(f.read())
    #print(encodedZip.decode())

jsonStuff = [
    {
        'PlaceHolder': "Base 64 String Goes Here"
    }
]

@app.route('/corGAN/api/image', methods=['GET'])
def get_tasks():
    return jsonify({'jsonStuff': jsonStuff})

if __name__ == '__main__':
    app.run(debug=True)