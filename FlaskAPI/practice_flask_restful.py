'''
Created on 2022年4月1日

@author: ning_lin
'''
import socket
from flask import Flask, jsonify, request, send_from_directory, abort
from flask_restful import Resource, Api, reqparse

from pydataset import data
import os

# ====================================================================================================
app = Flask(__name__)
api = Api(app)


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


class ShowIP(Resource):
    def get(self):
        try:
            ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
            data = {'ip': ip}
            return jsonify(data)
        except Exception:
            print("Didn't get ip.")


class GetData(Resource):
    def get(self):
        sex = request.args.get('sex')
        age = request.args.get('age')
        df = data('titanic')
        df = df[(df.sex == sex) & (df.age == age)].reset_index()
        df = df.to_json(orient='columns')
        return jsonify(df)


class PostData(Resource):
    def post(self):
        args_dict = request.get_json()
        sex = args_dict['sex']
        age = args_dict['age']
        df = data('titanic')
        df = df[(df.sex == sex) & (df.age == age)].reset_index()
        df = df.to_json(orient='columns')
        return jsonify(df)


class DownloadData(Resource):
    def get(self, filename):
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


# adding the defined resources along with their corresponding urls
api.add_resource(ShowIP, '/')
api.add_resource(GetData, '/get_data')
api.add_resource(PostData, '/post_data')
api.add_resource(DownloadData, '/download/<filename>')
# api.add_resource(DownloadData, '/download/<int:id>') 默認是文字，數字才要特別定義

if __name__ == '__main__':
    HOST = get_server_ip_address()
    PORT = 12340
    app.run(HOST, debug=True, port=PORT, ssl_context='adhoc')
