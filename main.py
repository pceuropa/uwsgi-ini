"""
File: main.py
Author: Rafal Marguzewicz
Email: info@pceuropa.net
Github: https://github.com/pceuropa/uwsgi-ini
Description: Examples: falcon, uwsgi.ini
"""

from json import loads, dumps
import falcon
from wsgiref import simple_server


class Parent(object):
    """Class to extends. Have two method load json data from post and default get method"""

    def json_load(self, req):
        return loads(str(req.stream.read().decode("utf-8")))

    def on_get(self, req: falcon.Request, resp: falcon.Response):
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = dumps({"success": "true"})


class View(Parent):
    pass


app = falcon.API()
view = View()
app.add_route('/', view)


if __name__ == '__main__':
    # run without uWsgi
    httpd = simple_server.make_server('127.0.0.1', 8000, app)
    print("http://127.0.0.1:8000")
    httpd.serve_forever()
