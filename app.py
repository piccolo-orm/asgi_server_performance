from starlette.endpoints import HTTPEndpoint
from starlette.responses import PlainTextResponse
from starlette.routing import Router, Route


class Home(HTTPEndpoint):
    def get(self, request):
        return PlainTextResponse("Hello")


app = Router(routes=[Route("/", Home)])
