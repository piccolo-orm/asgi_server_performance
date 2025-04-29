from starlette.applications import Starlette
from starlette.endpoints import HTTPEndpoint
from starlette.responses import PlainTextResponse
from starlette.routing import Route


class Home(HTTPEndpoint):
    def get(self, request):
        return PlainTextResponse("Hello")


starlette_app = Starlette(routes=[Route("/", Home)])


# Now wrap this into a top-level ASGI app callable
async def app(scope, receive, send):
    await starlette_app(scope, receive, send)
