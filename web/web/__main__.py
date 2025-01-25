from aiohttp import web
import aiohttp_cors

from .routes import routes


def start_web_server():
    app = web.Application()
    app.add_routes(routes)
    cors = aiohttp_cors.setup(app, defaults={
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*"
        )
    })

    for route in list(app.router.routes()):
        cors.add(route)
    web.run_app(app)


if __name__ == '__main__':
    start_web_server()
