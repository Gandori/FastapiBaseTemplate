import uvicorn
from api.api import api

class Base:
    def __init__(self, app, host, port, reload) -> None:
        self.app = app
        self.host = host
        self.port = port
        self.reload = reload

    def run(self):
        uvicorn.run(app=self.app, host=self.host, port=self.port, reload=self.reload)

if __name__ == "__main__":
    Base('run:api', '0.0.0.0', 8080, True).run()