from flask import Flask
from flask import request
import json

application = Flask(__name__)

def model(data):
    return data + 1
@application.route('/',methods=['POST'])
def hello_world():
    d = request.data
    dic = json.loads(d)
    num = dic['id']
    result = model(num)
    return str(result)


if __name__ == '__main__':
    application.run()
