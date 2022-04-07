'''
Created on 2022撟�4���1�

@author: ning_lin
'''

import socket
from flask import Flask, request, jsonify, send_from_directory, abort
from flask_cors import CORS

from pydataset import data
import os

# ====================================================================================================
app = Flask(__name__)
CORS(app, supports_credentials=True)


def get_server_ip_address():
    """
    get system ip address in case of changing system
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # connect to a global target
    s.connect(("8.8.8.8", 80))
    ip_addr = (s.getsockname()[0])
    s.close()
    return ip_addr


@app.route("/", methods=['GET', 'POST'])
def main():
    try:
        ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
        data = {'ip': ip}
        return jsonify(data)
    except Exception:
        print("Didn't get ip.")
# https://your_ip:12340/

@app.route("/get_data", methods=['GET'])
def get_data():
    sex = request.args.get('sex')
    age = request.args.get('age')
    df = data('titanic')
    df = df[(df.sex == sex) & (df.age == age)].reset_index()
    df = df.to_json(orient='columns')
    return jsonify(df)
# https://your_ip:12340/get_data?sex=man&age=adults


@app.route("/post_data", methods=['POST'])
def post_data():
    args_dict = request.get_json()
    sex = args_dict['sex']
    age = args_dict['age']
    df = data('titanic')
    df = df[(df.sex == sex) & (df.age == age)].reset_index()
    df = df.to_json(orient='columns')
    return jsonify(df)
# https://your_ip:12340/post_data


@app.route("/download/<filename>", methods=['GET', 'POST'])
def download_data_in_folder(filename):
    '''
    讓別人下載檔案的資料夾路境
    透過 flask 內建的 send_from_directory + as_attachment=True 做檔案下載的動作
    as_attachment=False 為開啟檔案，不是下載
    '''
    dirpath = os.path.join(app.root_path, 'download')
    try:
        return send_from_directory(dirpath, filename, as_attachment=True)
    except FileNotFoundError:
        abort(404)
# https://your_ip:12340/download/test_attach_text.txt

if __name__ == "__main__":
    '''
    獲取 server ip 及自定義 port（建議五碼較不會跟其他功能衝突）
    利用 run 來觸發 api
    ssl_context='adhoc' 為一臨時憑證，並須安裝套件 cryptography 才能使用
    '''
    HOST = get_server_ip_address()
    PORT = 12340
    app.run(HOST, debug=True, port=PORT, ssl_context='adhoc')
