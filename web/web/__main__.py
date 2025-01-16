from aiohttp import web

from .routes import routes


def start_web_server():
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app)


if __name__ == '__main__':
    start_web_server()
