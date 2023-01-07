import uvicorn
from api.api import api

class Server:
    def __init__(self, app, host, port):
        self.app = app
        self.host = host
        self.port = port

    def run(self):
        uvicorn.run(
            app=self.app,
            host=self.host,
            port=self.port
        )

if __name__ == "__main__":
    Server(app=api, host='0.0.0.0', port=8080).run()