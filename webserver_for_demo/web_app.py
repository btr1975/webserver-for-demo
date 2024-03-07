"""
FastAPI WebApp
"""

import os
from fastapi.staticfiles import StaticFiles

from fastapi import FastAPI
from webserver_for_demo.version import __version__
from webserver_for_demo.routers import example

from webserver_for_demo.routers import hello_world

static_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static')


# Used to config swagger UI
# Reference : https://swagger.io/docs/open-source-tools/swagger-ui/usage/configuration/
swagger_ui_parameters = {
    'docExpansion': 'none',
    'filter': 'true'
}

web_app = FastAPI(title='webserver-for-demo', version=__version__,
                  description='Just a Webserver for Demo', swagger_ui_parameters=swagger_ui_parameters)
web_app.include_router(example.router)

web_app.include_router(hello_world.router)

web_app.mount("/static", StaticFiles(directory=static_path), name="static")
