#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/9 13:59

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from git import Repo
import os, traceback
from pprint import pprint


class CustomHTTPHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        data_str = self.rfile.read(int(self.headers['Content-Length']))
        data_json = json.loads(data_str)
        pprint(data_json)
        repo_name = data_json["repository"]["name"]

        _repo = None
        _sv_local_repo = repo_name
        if not os.path.exists(_sv_local_repo):
            try:
                _repo = Repo.clone_from(GIT_URL.format(repo_name), _sv_local_repo)
                print("clone git repo {} success".format(repo_name))
            except Exception as e:
                print("clone git repo {} error".format(repo_name))
                traceback.print_exc()
                return
        else:
            _repo = Repo(_sv_local_repo)
            _repo.remote().pull()

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        response_data = {
            "result": "OK",
            "message": ""
        }
        self.wfile.write(bytes(json.dumps(response_data), encoding="utf-8"))
        return


HOST = "脚本部署服务器的IP"
PORT = 8891
GIT_URL = "http://gogs服务器IP:端口/microservice/{}.git"


def start_server(h, p):
    print("listen on (%s,%s)"%(h, p))
    http_server = HTTPServer((h, p), CustomHTTPHandler)
    http_server.serve_forever()


if __name__ == '__main__':
    start_server(HOST, PORT)